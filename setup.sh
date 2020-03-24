#!/bin/bash

git submodule init
git submodule update
python3 -m venv ./venv
source ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

curl -sL https://firebase.tools | bash

cd blog/
pelican-themes -i ../pelican-sober
