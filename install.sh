#!/bin/sh

apt install libgconf2.0
apt install libnss3
apt install libgtk2.0
apt install libasound2
apt install xvfb

conda install -c plotly plotly-orca poppler
python3 config.py