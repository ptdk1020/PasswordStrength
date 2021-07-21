import pandas as pd
import numpy as np

# from gensim.models import fasttext

import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
# from fasttext_model import wv

# print(wv.most_similar('password'))

app = dash.Dash(__name__)

# -------- import clean data ----------------
df = pd.read_csv('../data/password.csv')
df = df[df.length < 40]

# getting zxcvbn strength options
D_zxcvbn = []
for s in sorted(df.zxcvbn.unique()):
    D_zxcvbn.append({'label': str(s), 'value': s})

# -------- app layout -----------------------
app.layout = html.Div(
    children= [
        html.H1('Password visualization', style={'text-align':'center'}),
        dcc.Dropdown(id='select-zxcvbn-score', options=D_zxcvbn, multi=False, value=0),
        html.Br(),
        dcc.Graph(id='zxcvbn-chart'),
        html.Br(),
        #html.P(print(model['password']))
],
    className='wrapper'
)

# --------connect graphs with dash components------
@app.callback(
    Output("zxcvbn-chart", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_zxcvbn(score):
    dff = df.copy()
    dff = dff.groupby(['zxcvbn', 'length']).count().reset_index()
    dff = dff[dff.zxcvbn == score]

    fig = px.bar(data_frame=dff,
                 x='length',
                 y='index',
                 hover_data=['length', 'index'],
                 #template='plotly_dark'
                 )
    fig.update_layout(yaxis_title='count')

    return fig

# @app.callback(
#     Output("zxcvbn-chart2", "figure"),
#     [Input(component_id='select-zxcvbn-score', component_property='value')]
# )
# def update_zxcvbn2(score):
#     dff = df.copy()
#     dff = dff.groupby(['zxcvbn', 'length']).count().reset_index()
#     dff = dff[dff.zxcvbn == ((score+1)%4)]
#
#     fig = px.bar(data_frame=dff,
#                  x='length',
#                  y='index',
#                  hover_data=['length', 'index'],
#                  #template='plotly_dark'
#                  )
#     return fig



if __name__ == "__main__":
    app.run_server(debug=True)