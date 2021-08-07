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
frame_path = '../data/data2use/USA2/data0.csv'
reduction_file = '../data/data2use/USA2/reduction/freq_100_10_clus.csv'

df = pd.read_csv(frame_path)
df = df.iloc[:100000, :]
dff = pd.DataFrame(df[['password','frequency']].iloc[:1000,:])
rd = pd.read_csv(reduction_file)
# rd['zxcvbn'] = rd['zxcvbn'].astype('string')

# --------app-----------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('AI insights into Passwords', style={'text-align': 'left', 'font-family': 'sans-serif'}),
        html.P('This page is best viewed in full size window', style={'text-align': 'left', 'font-family': 'sans-serif',
                                                                      'font-size': '15px', 'font-style': 'italic'}),
        html.Div(
           [
               html.Div(
                   [
                       html.Img(src=app.get_asset_url('/images/password_card.jpg'),
                                style={'width': '300px', 'height': '200px', }),
                       html.Br(),
                       dbc.Card([
                           # dbc.CardImg(src="/assets/images/password_card.jpg", top=True),
                           dbc.CardBody([
                               html.H4("Introduction"),
                               html.P(
                                   """
                                   This dashboard contains some insights on a dataset of leaked passwords. 
                                   It is divided into two parts. 
                                   The first shows several statistical charts, filtered by zxcvbn score, which is an 
                                   algorithmic score developed by Dropbox. 
                                   The second part includes our password visualization result, in both 2 and 3
                                   dimensions.
                                    """),
                           ]),
                       ],  # className='boxdiv',
                           style={#'width': '80vh', 'height': '40vh',
                                  'vertical-align': 'top', 'font-family': 'sans-serif','width': ' 60vh'}
                       ),
                   ], style={'vertical-align': 'top', 'display': 'inline-block', 'width': '132.5vh', 'height': '40vh',}
               ),
               html.Div([
                   html.Label("Top 1000 most frequent passwords"),
                   dash_table.DataTable(
                   id='top-100-passwords',
                   columns=[{'id': c, 'name': c} for c in dff.columns],
                   page_size=10,
                   data= dff.to_dict('records'),
                   style_as_list_view=True,
                   style_header={'backgroundColor': '#ADD8E6', 'fontWeight': 'bold'},
               )], className='boxdiv',
                   style={'display': 'inline-block', 'width': ' 50vh', 'height': '40vh',
                          'font-family': 'sans-serif', 'horizontal-align': 'right'}
               )
           ], #className='boxdiv'
        ),
        html.Div([
                html.H4('Some password statistics', style={'font-family': 'sans-serif'}),
                html.P(
                """
                Given a choice of a zxcvbn score, this section contains several statistical charts on the top 
                100000 most frequent passwords in the dataset. 
                For password categories,
                the definitions are as follows: alphabetic (at least 80% letters), numeric (at least 80% digits), 
                and mixed (at least 30% letters, at least 30% digits). Also, a password is policy compliant if it
                 is at least 8 characters long anf if it contains at least 1 lowercase letter, 1 uppercase letter, 
                 1 digit, and 1 special character. 
                """,
                       style={'font-family': 'sans-serif', 'width': ' 70vh'}),
                html.Br(),
                html.Label('Choose zxcvbn score:', style={'font-family': 'sans-serif', 'display': 'inline-block'}),
                dcc.Dropdown(id='select-zxcvbn-score',
                     options=[
                        {'label': '0', 'value': 0},
                        {'label': '1', 'value': 1},
                        {'label': '2', 'value': 2},
                        {'label': '3', 'value': 3},
                        {'label': '4', 'value': 4}
                             ],
                     value=0,
                     style={'verticalAlign': 'middle', 'display': 'inline-block', 'width': '33%', 'font-family': 'sans-serif'}
                 ),
                html.Br(),
                dcc.Graph(id='zxcvbn-chart-1', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-2', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-3', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                html.Br(),
                dcc.Graph(id='zxcvbn-chart-4', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-5', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-6', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                html.Br(),
                ], className='boxdiv'),
        html.Div([
                html.H4('Password embedding visualization', style={'font-family': 'sans-serif'}),
                html.P(
                    """
                    This section contains our visualization result on passwords with frequency at least 100. 
                    Via a fastText embedding, we represented 
                    passwords as 300-dimensional vectors. Using UMAP or t-SNE, we visualize this embedding in 
                    2 and 3 dimensions. We include additional filters for various password chracteristics.
                    """,
                       style={'font-family': 'sans-serif', 'width': ' 70vh'}),
                html.Label('Choose reduction map:', style={'verticalAlign': 'middle', 'display': 'inline-block', 'font-family': 'sans-serif'}),
                dcc.Dropdown(id='select-embedding',
                        options=[
                             {'label': 'UMAP', 'value': 'umap'},
                             {'label': 't-SNE', 'value': 'tsne'},
                         ],
                             value='umap',
                         style={'verticalAlign': 'middle', 'display': 'inline-block', 'width': '33%', 'font-family': 'sans-serif'}
                         ),
                html.Label('Additional filters:', style={'verticalAlign': 'middle', 'display': 'inline-block', 'font-family': 'sans-serif'}),
                dcc.Dropdown(id='select-column',
                        options=[
                             {'label': 'Password topic', 'value': 'topic'},
                             #{'label': 'Policy compliance', 'value': 'passpolicy'},
                             {'label': 'zxcvbn score', 'value': 'zxcvbn'},
                             {'label': 'Password category', 'value': 'category'},
                             {'label': 'First character', 'value': 'first_char'},
                             {'label': 'Last character', 'value': 'last_char'},
                             {'label': 'length', 'value': 'passlength'}
                         ],
                         style={'verticalAlign': 'middle', 'display': 'inline-block', 'width': '33%', 'font-family': 'sans-serif'}
                         ),
                dcc.Graph(id='embedding-2d',
                          style={'display': 'inline-block', 'width': '150vh', 'height': '100vh', 'font-family': 'sans-serif'}),
                dcc.Graph(id='embedding-3d',
                          style={'display': 'inline-block', 'width': '150vh', 'height': '100vh', 'font-family': 'sans-serif'}),
        ], className='boxdiv'),

    ],
    className='wrapper'
)


# --------connect graphs with dash components------

@app.callback(
    Output("zxcvbn-chart-1", "figure"),
    Output("zxcvbn-chart-2", "figure"),
    Output("zxcvbn-chart-3", "figure"),
    Output("zxcvbn-chart-4", "figure"),
    Output("zxcvbn-chart-5", "figure"),
    Output("zxcvbn-chart-6", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_graphs(score):
    # figure 1
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'category']).count().reset_index()
    frame = frame[['zxcvbn', 'category', 'frequency']]
    frame = frame[frame.zxcvbn == score]

    fig1 = px.pie(data_frame=frame,
                 names='category',
                 values='frequency',
                 color_discrete_sequence=px.colors.qualitative.T10,
                 title='Distribution of password categories'
                 )

    # figure 2
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'first_char']).count().reset_index()
    frame = frame[['zxcvbn', 'first_char', 'frequency']]
    frame = frame[frame.zxcvbn == score]

    fig2 = px.pie(data_frame=frame,
                 names='first_char',
                 values='frequency',
                 color_discrete_sequence=px.colors.qualitative.T10,
                 title='Distribution of first character types'
                 )

    # figure 3
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'last_char']).count().reset_index()
    frame = frame[['zxcvbn', 'last_char', 'frequency']]
    frame = frame[frame.zxcvbn == score]

    fig3 = px.pie(data_frame=frame,
                  names='last_char',
                  values='frequency',
                  color_discrete_sequence=px.colors.qualitative.T10,
                  title='Distribution of last character types'
                  )

    # figure 4
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'passlength']).count().reset_index()
    frame = frame[['zxcvbn', 'passlength', 'frequency']]
    frame = frame[frame.zxcvbn == score]

    fig4 = px.bar(data_frame=frame,
                  x='passlength',
                  y='frequency',
                  color_discrete_sequence=px.colors.qualitative.T10,
                  title='Distribution of password lengths'
                  )
    fig4.update_layout(xaxis_title='password lengths')

    # figure 5
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'number_of_uppercase']).count().reset_index()
    frame = frame[['zxcvbn', 'number_of_uppercase', 'frequency']]
    frame['log'] = np.log(1+frame['frequency'])
    frame = frame[frame.zxcvbn == score]

    fig5 = px.bar(data_frame=frame,
                 x='number_of_uppercase',
                 y='log',
                 color_discrete_sequence=px.colors.qualitative.T10,
                 title='Log distribution of number of uppercase'
                 )
    fig5.update_layout(xaxis_title='number of uppercase letters')
    fig5.update_layout(yaxis_title='logarithmic frequency')

    # figure 6
    frame = df.copy()
    frame = frame.groupby(['zxcvbn', 'passpolicy']).count().reset_index()
    frame = frame[['zxcvbn', 'passpolicy', 'frequency']]
    frame['log'] = np.log(1 + frame['frequency'])
    frame = frame[frame.zxcvbn == score]

    fig6 = px.bar(frame, x='passpolicy',
                  y='log',
                  color_discrete_sequence=px.colors.qualitative.T10,
                  title='Log distribution of policy compliant passwords')
    fig6.update_layout(xaxis_title='compliant status')
    fig6.update_layout(yaxis_title='logarithmic frequency')

    return fig1, fig2, fig3, fig4, fig5, fig6


@app.callback(
    Output('embedding-2d', 'figure'),
    Output('embedding-3d', 'figure'),
    Input('select-column', 'value'),
    Input('select-embedding', 'value'),
)
def embedding_plots(col, map):
    frame = rd.copy()

    if map == 'umap':
        fig2d = px.scatter(data_frame=frame , x='x_2u', y='y_2u', color=col,
                         color_discrete_sequence=px.colors.qualitative.T10,
                         hover_data=['password'],
                           title='Embedding 2D')
        fig3d = px.scatter_3d(data_frame=frame, x='x_3u', y='y_3u', z='z_3u', color=col,
                           color_discrete_sequence=px.colors.qualitative.T10,
                           hover_data=['password'],
                              title='Embedding 3D')
    elif map == 'tsne':
        fig2d = px.scatter(data_frame=frame, x='x_2t', y='y_2t', color=col,
                           color_discrete_sequence=px.colors.qualitative.T10,
                           hover_data=['password'],
                           title='Embedding 2D')
        fig3d = px.scatter_3d(data_frame=frame, x='x_3t', y='y_3t', z='z_3t', color=col,
                              color_discrete_sequence=px.colors.qualitative.T10,
                              hover_data=['password'],
                              title='Embedding 3D')
    fig2d.update_layout(xaxis_title='x',yaxis_title='y')
    fig3d.update_layout(scene = dict(xaxis_title='x', yaxis_title='y', zaxis_title='z'))

    return fig2d, fig3d


if __name__ == "__main__":
    app.run_server(debug=True)