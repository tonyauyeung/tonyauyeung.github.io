#!/usr/bin/env bash
# Compile assets/resume/resume.tex → assets/pdf/Tony_CV.pdf
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
RESUME_DIR="${ROOT}/assets/resume"
PDF_DIR="${ROOT}/assets/pdf"
OUTPUT="${PDF_DIR}/Tony_CV.pdf"

if ! command -v pdflatex >/dev/null 2>&1; then
  echo "error: pdflatex not found. Install a TeX distribution (e.g. MacTeX or texlive)." >&2
  exit 1
fi

python3 "${ROOT}/bin/generate-resume-publications.py"
python3 "${ROOT}/bin/generate-resume-academic-service.py"

mkdir -p "${PDF_DIR}"
cd "${RESUME_DIR}"

for _ in 1 2; do
  pdflatex -interaction=nonstopmode -output-directory="${PDF_DIR}" resume.tex >/dev/null
done

mv -f "${PDF_DIR}/resume.pdf" "${OUTPUT}"
rm -f "${PDF_DIR}/resume.aux" "${PDF_DIR}/resume.log" "${PDF_DIR}/resume.out"

echo "Built ${OUTPUT}"
