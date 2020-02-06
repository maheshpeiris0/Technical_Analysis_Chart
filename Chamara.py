# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 14:24:42 2017

@author: maheshp
"""

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

a1 = pd.ExcelFile("SP.xlsx")
df = a1.parse("Sheet1")
x1 = df["Date"]
y1 = df["MCO"]
y2 = df['IBM']
y3 = df['GOOG']
y4 = df['C']




trace0 = go.Scatter( x=x1,y=y1,name='MCO',line = dict(color=('rgb(0, 0, 255)')))
trace1 = go.Scatter(x=x1, y=y2, line = dict(color=('rgb(49,255,110)')),name='IBM',yaxis='y2')
trace2 = go.Scatter(x=x1,y=y3, mode='line',name='GOOG',yaxis='y3')
trace3 = go.Scatter(x=x1,y=y4, mode='line',name='C',yaxis='y4')

data = [trace0, trace1,trace2,trace3]
layout = go.Layout(title='Multiple Y Axis Example',
                   
                  annotations=[
        dict(
            x='2011-12-30',
            y=50,
            #xanchor='right',
            xref='x',
            yref='y',
            #xshift = 12,
            #overlaying='y',side='right',position=0.90,
            text='Mahesh',
            showarrow=False,
            font=dict(
                family='Courier New, monospace',
                size=16,
                color='#ffffff'
            ),
            align='center',
            arrowhead=2,
            arrowsize=1,
            arrowwidth=2,
            arrowcolor='#636363',
            ax=200,
            ay=30,
            bordercolor='#c7c7c7',
            borderwidth=2,
            borderpad=4,
            bgcolor='#ff7f0e',
            opacity=0.8
        )
    ],                                      
                   
                   xaxis= dict(domain=[0.1,0.8]),
                   yaxis=dict(side='right',showgrid=False,showline=True,linecolor='rgb(0, 0, 0)',linewidth=1), yaxis2=dict(overlaying='y',side='right',position=0.85,showgrid=False,showline=True,linecolor='rgb(0, 0, 0)',linewidth=1),
                   yaxis3=dict(overlaying='y',side='right',position=0.90,showgrid=False,showline=True,linecolor='rgb(0, 0, 0)',linewidth=1),
                              yaxis4=dict(overlaying='y',side='right',position=0.95,showgrid=False, showline=True,linecolor='rgb(0, 0, 0)',linewidth=1))



fig =go.Figure(data=data, layout=layout)
#py.iplot(data, filename='Chamara')
py.plot(fig, filename='Chamara1')





