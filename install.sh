#!/bin/sh

apt install libgtk2.0
apt install xvfb

conda install -c plotly plotly-orca
python3 config.py