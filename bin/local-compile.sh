#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
REQUIRED_RUBY_VERSION="3.3.5"
cd "${PROJECT_ROOT}"

usage() {
    cat <<'USAGE'
Usage: ./bin/local-compile.sh [options]

Options:
  --build         Build site only (no local server).
  --install       Install local dependencies (Ruby + Python) and exit.
  --docker        Force Docker compose for local preview/build.
  --port <port>   Override local port for non-Docker server (default: 4000).
  --host <host>   Override host for local server (default: 127.0.0.1).
  -h, --help     Show this message.

Default action is to start local Jekyll server with watch/livereload.
On macOS systems with old system Ruby (2.x), use `--docker`.
USAGE
}

MODE="serve"
USE_DOCKER=0
HOST="127.0.0.1"
PORT="4000"

while [[ $# -gt 0 ]]; do
    case "$1" in
        --build)
            MODE="build"
            shift
            ;;
        --install)
            MODE="install"
            shift
            ;;
        --docker)
            USE_DOCKER=1
            shift
            ;;
        --port)
            PORT="$2"
            shift 2
            ;;
        --host)
            HOST="$2"
            shift 2
            ;;
        -h|--help)
            usage
            exit 0
            ;;
        *)
            echo "Unknown option: $1"
            usage
            exit 1
            ;;
    esac
done

run_docker() {
    local compose_cmd
    local compose_bin

    if command -v docker >/dev/null 2>&1 && docker compose version >/dev/null 2>&1; then
        compose_cmd="compose"
    elif command -v docker-compose >/dev/null 2>&1; then
        compose_cmd="compose-legacy"
        compose_bin="docker-compose"
    elif [ -x /Applications/Docker.app/Contents/Resources/bin/docker-compose ]; then
        compose_cmd="compose-legacy"
        compose_bin="/Applications/Docker.app/Contents/Resources/bin/docker-compose"
    else
        echo "No docker compose executable found."
        if command -v docker >/dev/null 2>&1; then
            echo "Install docker compose plugin or Docker Desktop and retry."
            echo "Run: brew install docker-compose            # legacy compose"
            echo "      brew install docker-compose-switch     # switch plugin if needed"
        else
            echo "Install Docker Desktop and retry:"
            echo "  brew install --cask docker"
            echo "  open -a Docker"
            echo "Then run: ./bin/local-compile.sh --docker --build"
        fi
        exit 1
    fi

    if [[ "${MODE}" == "build" ]]; then
        if [[ "${compose_cmd}" == "compose" ]]; then
            docker compose run --rm jekyll bundle exec jekyll build
        else
            "${compose_bin}" run --rm jekyll bundle exec jekyll build
        fi
    else
        if [[ "${compose_cmd}" == "compose" ]]; then
            if ! docker compose pull; then
                echo "Pull failed (network/TLS issue); falling back to local docker build."
                docker compose up --build
            else
                docker compose up
            fi
        else
            if ! "${compose_bin}" pull; then
                echo "Pull failed (network/TLS issue); falling back to local docker build."
                "${compose_bin}" up --build
            else
                "${compose_bin}" up
            fi
        fi
        echo "If your container is running, open http://localhost:8080"
    fi
    exit 0
}

if [[ "${USE_DOCKER}" -eq 1 ]]; then
    run_docker
fi

ensure_cmd() {
    if ! command -v "$1" >/dev/null 2>&1; then
        echo "Missing required command: $1"
        exit 1
    fi
}

ensure_cmd bundle
ensure_cmd ruby
ensure_cmd python3

current_ruby_version="$(ruby -e 'print RUBY_VERSION')"
if ! ruby -e "exit(Gem::Version.new('$current_ruby_version') >= Gem::Version.new('$REQUIRED_RUBY_VERSION') ? 0 : 1)" >/dev/null 2>&1; then
    echo "Current Ruby is ${current_ruby_version}; al-folio CI uses Ruby ${REQUIRED_RUBY_VERSION}."
    if command -v docker >/dev/null 2>&1; then
        echo "Falling back to Docker-based local build (recommended on this machine)."
        run_docker
    fi

    echo "Your Ruby is too old for this project's Gemfile lock and theme plugins."
    echo "Install Ruby ${REQUIRED_RUBY_VERSION} and rerun, or set USE_DOCKER by running:"
    echo "  ./bin/local-compile.sh --docker"
    if command -v brew >/dev/null 2>&1; then
        echo "Quick fix on macOS:"
        echo "  brew install ruby@3.3"
    fi
    exit 1
fi

bundler_version() {
    awk '/^BUNDLED WITH/{getline; gsub(/^[[:space:]]+/, "", $0); gsub(/[[:space:]]+$/, "", $0); print; exit}' Gemfile.lock
}

ensure_bundler() {
    local required_bundler
    local user_gem_bin

    required_bundler="$(bundler_version)"
    if [[ -z "${required_bundler}" ]]; then
        required_bundler="2.6.2"
    fi

    if command -v "bundle" >/dev/null 2>&1; then
        if bundle _${required_bundler}_ --version >/dev/null 2>&1; then
            return 0
        fi
    fi

    echo "Installing Bundler ${required_bundler} for Ruby ${current_ruby_version}..."
    if ! gem install --user-install --no-document "bundler:${required_bundler}"; then
        echo "Bundler install failed. You can either install Ruby ${REQUIRED_RUBY_VERSION} locally or use --docker."
        exit 1
    fi

    user_gem_bin="$(ruby -e 'print Gem.user_dir')/bin"
    export PATH="${user_gem_bin}:${PATH}"

    if ! bundle _${required_bundler}_ --version >/dev/null 2>&1; then
        echo "Bundler ${required_bundler} still not available. Falling back to Docker."
        run_docker
    fi
}

install_deps() {
    ensure_bundler
    bundle config set --local path vendor/bundle
    bundle check || bundle install
    python3 -m pip install -r requirements.txt
}

run_jekyll() {
    bundle exec jekyll "$@"
}

case "${MODE}" in
    install)
        ensure_cmd gem
        install_deps
        echo "Dependencies installed."
        ;;
    build)
        install_deps
        run_jekyll build
        ;;
    serve)
        install_deps
        if command -v pdflatex >/dev/null 2>&1; then
            ./bin/build-resume.sh
        else
            echo "pdflatex not found, skipping resume regeneration."
        fi
        run_jekyll serve \
            --host "${HOST}" \
            --port "${PORT}" \
            --watch \
            --livereload
        ;;
    *)
        echo "Unknown mode: ${MODE}"
        exit 1
        ;;
esac
