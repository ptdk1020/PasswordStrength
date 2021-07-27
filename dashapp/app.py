import pandas as pd
import numpy as np

import plotly.express as px

import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output

# ---------gensim-stuff---------------------

# ---------end-of-gensim-stuff---------------

# -------- import clean data ----------------
df = pd.read_csv('../data/data2use/USA2/data0.csv',index_col=0)
dff = pd.DataFrame(df[['password','frequency']].iloc[:200,:])

# getting zxcvbn strength options
D_zxcvbn = []
for s in sorted(df.zxcvbn.unique()):
    D_zxcvbn.append({'label': str(s), 'value': s})

# --------app-----------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('Visual insights into Passwords', style={'text-align': 'left'}),
        html.Div(
           [
               dbc.Card([
                   dbc.CardImg(src="/static/images/placeholder286x180.png", top=True),
                   dbc.CardBody([
                       html.H4("An examination of <file>"),
                       html.P("This is a high-level description of what we did."),
                    ]),
               ],
                   style={'display': 'inline-block','width': '60vh', 'height': '30vh'}
               ),
               html.Div([dash_table.DataTable(
                   id='top-100-passwords',
                   columns=[{'id': c, 'name': c} for c in dff.columns],
                   page_size=10,
                   data= dff.to_dict('records')
               )],
                   style={'display': 'inline-block','width': '60vh', 'height': '30vh'}
               )
           ]
        ),
        html.Div([
                    dcc.Dropdown(id='select-zxcvbn-score',
                         options=[
                            {'label': '0', 'value': 0},
                            {'label': '1', 'value': 1},
                            {'label': '2', 'value': 2},
                            {'label': '3', 'value': 3},
                            {'label': '4', 'value': 4}
                                 ],
                            value=0,
                         style={'width': '70%'}
                     ),
                    dcc.Graph(id='zxcvbn-chart', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                    dcc.Graph(id='zxcvbn-chart-2',style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                    dcc.Graph(id='zxcvbn-chart-3',style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'})
                  ]),
    ],
    className='wrapper'
)


# --------connect graphs with dash components------
@app.callback(
    Output("zxcvbn-chart", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_zxcvbn(score):
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'category']).count().reset_index()
    frame = frame[['zxcvbn', 'category', 'frequency']]
    frame = frame[frame.zxcvbn == score]

    fig = px.pie(data_frame=frame,
                 names='category',
                 values='frequency',
                 #hover_data=['category', 'frequency'],
                 #template='plotly_dark'
                 )
    # fig.update_layout(yaxis_title='count')
    return fig


@app.callback(
    Output("zxcvbn-chart-2", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_zxcvbn_2(score):
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'number_of_symbols']).count().reset_index()
    frame = frame[['zxcvbn', 'number_of_symbols', 'frequency']]
    frame['log'] = np.log(1+frame['frequency'])
    frame = frame[frame.zxcvbn == score]

    fig = px.bar(data_frame=frame,
                 x='number_of_symbols',
                 y='log',
                 #hover_data=['category', 'frequency'],
                 #template='plotly_dark'
                 )
    fig.update_layout(yaxis_title='log count')
    return fig


@app.callback(
    Output("zxcvbn-chart-3", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_zxcvbn_3(score):
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'passlength']).count().reset_index()
    frame = frame[['zxcvbn', 'passlength', 'frequency']]
    # frame['log_count'] = np.log(frame['frequency'])
    frame = frame[frame.zxcvbn == score]

    fig2 = px.bar(data_frame=frame,
                 x='passlength',
                 y='frequency',
                 #hover_data=['category', 'frequency'],
                 #template='plotly_dark'
                 )
    # fig.update_layout(yaxis_title='count')
    return fig2


if __name__ == "__main__":
    app.run_server(debug=True)