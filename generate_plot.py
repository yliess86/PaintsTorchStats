import plotly.graph_objs as go
import plotly.plotly as py
import plotly.io as pio
import pandas as pd
import numpy as np
import json
import os

from plotly.offline import plot

NAME2PATH = {
    '[Paper]: Random, Simple'          : './data/paper_random_simple.csv',
    '[Paper]: Strokes, Simple'         : './data/paper_strokes_simple.csv',
    '[Paper]: Strokes, Double'         : './data/paper_strokes_double.csv',

    '[Custom]: Strokes, Simple'        : './data/custom_strokes_simple.csv',
    '[Custom]: Strokes, Double'        : './data/custom_strokes_double.csv',

    '[Custom + Paper]: Strokes, Double': './data/custom_and_paper_strokes_double.csv',
}

NAME2CSV  = {
    name: pd.read_csv(path, sep=';', index_col=0, names=['ID', 'FID', 'STD'])
    for (name, path) in NAME2PATH.items()
}

NAME2DATA = {
    name: { 'FID': csv['FID'].values, 'STD': csv['STD'].values }
    for (name, csv) in NAME2CSV.items()
}
X         = list(range(0, 120, 20))
COLORS    = [
    'rgb(255, 0, 145)',
    # 'rgb(211, 108, 235)',
    'rgb(118, 164, 255)',
    # 'rgb(0, 202, 255)',
    'rgb(0, 227, 255)',
    # 'rgb(0, 234, 235)',
    'rgb(0, 238, 206)',
    # 'rgb(88, 240, 171)',
    'rgb(137, 224, 113)',
    # 'rgb(180, 204, 56)',
    'rgb(219, 178, 0)',
    # 'rgb(255, 144, 0)',
]

NAME2PLOT = {
    name: {
        'FID': go.Scatter(
            x    = X,
            y    = np.log(np.array(data['FID'])),
            line = dict(color=COLORS[i]),
            mode = 'lines',
            name = name
        )
    }
    for i, (name, data) in enumerate(NAME2DATA.items())
}

data   = [plot for plots in NAME2PLOT.values() for plot in plots.values()]
layout = go.Layout(
    paper_bgcolor='rgb(255,255,255)',
    plot_bgcolor='rgb(229,229,229)',
    # title='FID by Model over Epochs',
    xaxis=dict(
        title='Epochs',
        gridcolor='rgb(255,255,255)',
        range=[0, 100],
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
    yaxis=dict(
        title='log(FID)',
        gridcolor='rgb(255,255,255)',
        showgrid=True,
        showline=False,
        showticklabels=True,
        tickcolor='rgb(127,127,127)',
        ticks='outside',
        zeroline=False
    ),
)
fig = go.Figure(data=data, layout=layout)
# plot(fig)
# pio.write_image(fig, 'fid.eps')
pio.write_image(fig, 'fid.png')
