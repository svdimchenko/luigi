#!/usr/bin/env bash

echo "=========================================================================="
echo " Luigi environment  "
echo "=========================================================================="
PYTHON_VERSION="3.8"
ENV_DIR=".venv"

echo "--------------------------------------------------------------------------"
echo " --> Setup environment: Python version: ${PYTHON_VERSION}. Location: ${ENV_DIR}"
echo "--------------------------------------------------------------------------"
virtualenv -p python${PYTHON_VERSION} ${ENV_DIR}
source .venv/bin/activate
pip install --upgrade pip pip-tools
export PYTHONPATH="."

echo "--------------------------------------------------------------------------"
echo " --> Install dependencies:"
echo "--------------------------------------------------------------------------"
pip install -r requirements.txt
