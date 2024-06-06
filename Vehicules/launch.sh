#!/bin/sh

python3 -m venv env
source env/bin/activate
pip install osmnx 
pip install networkx
python3 ./main.py $1

