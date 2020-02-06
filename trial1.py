import plotly.plotly as py
import plotly.graph_objs as go
import pandas as pd

#df2 = pd.DataFrame([1, 2, 3, 2, 1, 3, 5])
data2 = list([1,2,3,4,5])

trace1 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
)
trace2 = go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
)
data = [trace1, trace2]
layout = go.Layout(
    showlegend=False,
    annotations=[
        dict(
            x=0,
            y=5,
            #xref='x',
            #yref='y',
            text=max(data2),
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
            ax=20,
            ay=-30,
            bordercolor='#c7c7c7',
            borderwidth=2,
            borderpad=4,
            bgcolor='#ff7f0e',
            opacity=0.8
        )
    ]
)
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='style-annotation')

