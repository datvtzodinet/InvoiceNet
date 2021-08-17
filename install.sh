#!/usr/bin/env bash

# install dependencies
sudo apt install -y python3-pip virtualenv tesseract-ocr poppler-utils libxext-dev libsm-dev libxrender-dev

# create virtual environment
virtualenv env -p python3
source env/bin/activate
pip install .
pip install google-cloud-vision
