#!/bin/bash
# Run all tests with coverage and generate HTML report
pytest --cov=toy --cov-report=html --html=report.html --self-contained-html
