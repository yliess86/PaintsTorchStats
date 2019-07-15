import plotly.graph_objs as go
import plotly.plotly as py
import plotly.io as pio
import pandas as pd
import numpy as np
import json
import os

from plotly.offline import plot

STUDY = pd.read_csv('./data/StudyDataset/study.csv', ';', names=('UUID', 'file_name', 'model', 'rate'))

DATA   = []
MODELS = ['PaperRS', 'CustomSS', 'CustomSD']

for model in MODELS:
    STD  = STUDY[STUDY.model == model].rate.std()
    MEAN = STUDY[STUDY.model == model].rate.mean()
    
    print(f'Model: {model}', f'Mean: {MEAN}', f'Std: {STD}')

for model in MODELS:
    DATA.append([
        len(STUDY[(STUDY.model == model) & (STUDY.rate == rate)]) 
        for rate in range(1, 6)
    ])
    

trace  = go.Heatmap(z=DATA, x=list(range(1, 6)), y=MODELS)
layout = go.Layout(
    paper_bgcolor='rgb(255,255,255)',
    xaxis=dict(
        title='MOS'
    ),
    yaxis=dict(
        title='Model'
    ),
)
fig    = go.Figure(data=tace, layout=layout)
pio.write_image(fig, 'heatmap.eps')
pio.write_image(fig, 'heatmap.png')