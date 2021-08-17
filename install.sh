#!/usr/bin/env bash

# install dependencies
sudo apt install -y python-pip python-virtualenv tesseract-ocr poppler-utils libxext-dev libsm-dev libxrender-dev

# create virtual environment
virtualenv env -p python3
source env/bin/activate
pip install google-cloud-vision
pip install .
