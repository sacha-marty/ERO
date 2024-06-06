#!/bin/sh

python -m venv env
source env/bin/activate
pip install -r matplotlib osmnx networkx
python ./main.py
