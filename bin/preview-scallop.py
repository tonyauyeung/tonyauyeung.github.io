#!/usr/bin/env python3
"""Build and preview the standalone SCALLOP page without Jekyll dependencies.

    python3 bin/preview-scallop.py
    python3 bin/preview-scallop.py --build-only

Jekyll copies this page unchanged because it has no YAML front matter.
This helper copies the same static files to _site/scallop for local preview.
"""

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import shutil


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--build-only", action="store_true")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    root = Path(__file__).resolve().parent.parent
    source = root / "scallop"
    output = root / "_site"
    shutil.copytree(source, output / "scallop", dirs_exist_ok=True)
    print("Built SCALLOP page: {}".format(output / "scallop"), flush=True)
    if args.build_only:
        return

    handler = partial(SimpleHTTPRequestHandler, directory=str(output))
    with ThreadingHTTPServer(("127.0.0.1", args.port), handler) as server:
        print("Preview: http://127.0.0.1:{}/scallop/".format(args.port), flush=True)
        print("Press Ctrl+C to stop.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    main()
