[![codecov](https://codecov.io/gh/yourusername/toy/branch/main/graph/badge.svg)](https://codecov.io/gh/yourusername/toy)

# Toy Package

A toy Python package for analyzing atmospheric river metrics, with modular structure, CLI access, unit testing, and Sphinx documentation.

---

## 📦 Project Structure

```
toy_package/
├── toy/                      # Main package
│   ├── api/                  # Class-based API modules
│   ├── utils/                # Core analytical functions
│   ├── cli.py                # Command-line interface entry
│   └── __init__.py
├── tests/                    # pytest-based tests
├── data/                     # Sample/test data files (.npy)
├── docs/                     # Sphinx documentation
├── .github/workflows/        # GitHub Actions CI/CD
├── pyproject.toml            # Build configuration
├── run_tests.sh              # Shell script to run tests and coverage
├── .readthedocs.yaml         # RTD configuration
├── MANIFEST.in               # Include data/doc files in builds (optional)
├── LICENSE                   # Project license
└── CITATION.cff              # Citation metadata
```

---

## 🛠 Installation

```bash
# Create and activate environment
conda env create -f environment.yml
conda activate toy_env

# Or install via pip (editable mode for dev)
pip install -e .
```

---

## 🚀 Run the CLI

```bash
toy --mode intensity --data 1.0 2.0 3.0
toy --mode trend --data 3.0 2.0 1.0
toy --mode max --data 1.0 2.0 3.0
toy --mode summary --data 1.0 2.0 3.0
```

If `toy` is not recognized, use:

```bash
python toy/cli.py --mode summary --data 1.0 2.0 3.0
```

---

## ✅ Run Tests

```bash
./run_tests.sh
```

Generates:
- `report.html` – test result report
- `htmlcov/` – coverage report

---

## 📚 Build Documentation

```bash
cd docs
sphinx-build -b html . _build/html
open _build/html/index.html
```

---

## 🚀 Deploy & CI/CD

- **Docs** auto-deploy to GitHub Pages via `.github/workflows/docs.yml`
- **Tests & Coverage** run via `.github/workflows/test.yml`
- **PyPI Publishing** supported with `git tag vX.Y.Z` and `PYPI_API_TOKEN` secret

---

## 🧪 Coverage

After running tests:

- View HTML: `htmlcov/index.html`
- Badge updates via Codecov in README

---

## 📖 Citation

See `CITATION.cff` or cite as:
```
Your Name (2025). toy: Atmospheric River Metrics Package (v0.1.0).
```
