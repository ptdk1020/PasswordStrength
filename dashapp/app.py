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
df = pd.read_csv('../data/data2use/USA2/data0.csv')
dff = pd.DataFrame(df[['password','frequency']].iloc[:200,:])

# tsne 2d
tsne2 = pd.read_csv('../data/data2use/Embedding/red_100_8_tsne_2.csv')
tsne2['label'] = tsne2['label'].astype('string')
tsne2d = px.scatter(data_frame=tsne2, x='x', y='y',color='label', title='t-SNE',
                    color_discrete_sequence=px.colors.qualitative.Prism,hover_data=['password'])

# umap 2d
umap2 = pd.read_csv('../data/data2use/Embedding/red_100_8_umap_2.csv')
umap2['label'] = umap2['label'].astype('string')
umap2d = px.scatter(data_frame=umap2, x='x', y='y',color='label', title='UMAP',
                    color_discrete_sequence=px.colors.qualitative.Prism,hover_data=['password'])

# tsne 3d
tsne3 = pd.read_csv('../data/data2use/Embedding/red_100_8_tsne_3.csv')
tsne3['label'] = tsne3['label'].astype('string')
tsne3d = px.scatter_3d(data_frame=tsne3, x='x', y='y', z='z', color='label', opacity=0.75,
                    color_discrete_sequence=px.colors.qualitative.Prism,hover_data=['password'])

# umap 3d
umap3 = pd.read_csv('../data/data2use/Embedding/red_100_8_umap_3.csv')
umap3['label'] = umap3['label'].astype('string')
umap3d = px.scatter_3d(data_frame=umap3, x='x', y='y', z='z', color='label', opacity =0.75,
                    color_discrete_sequence=px.colors.qualitative.Prism,hover_data=['password'])

# thres 10 + clusters
# c8 = pd.read_csv('../data/data2use/Embedding/red_10_8_umap_2.csv')
# c12 = pd.read_csv('../data/data2use/Embedding/red_10_12_umap_2.csv')
# c16 = pd.read_csv('../data/data2use/Embedding/red_10_16_umap_2.csv')

# --------app-----------------------
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        html.H1('Visual insights into Passwords', style={'text-align': 'left', 'font-family': 'sans-serif'}),
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
                               html.P("Describe dashboard"),
                           ]),
                       ],  # className='boxdiv',
                           style={#'width': '80vh', 'height': '40vh',
                                  'vertical-align': 'top', 'font-family': 'sans-serif'}
                       ),
                   ], style={'vertical-align': 'top', 'display': 'inline-block', 'width': '132.5vh', 'height': '40vh',}
               ),
               html.Div([
                   html.Label("Top 200 most frequent passwords"),
                   dash_table.DataTable(
                   id='top-100-passwords',
                   columns=[{'id': c, 'name': c} for c in dff.columns],
                   page_size=10,
                   data= dff.to_dict('records'),
                   style_as_list_view=True,
                   style_header={'backgroundColor': '#ADD8E6', 'fontWeight': 'bold'},
               )], className='boxdiv',
                   style={'display': 'inline-block', 'width': ' 60vh', 'height': '40vh',
                          'font-family': 'sans-serif', 'horizontal-align': 'right'}
               )
           ], #className='boxdiv'
        ),
        html.Div([
                html.H4('Some password statistics', style={'font-family': 'sans-serif'}),
                html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
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
                dcc.Graph(id='zxcvbn-chart', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-2', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                dcc.Graph(id='zxcvbn-chart-3', style={'display': 'inline-block', 'width': '60vh', 'height': '60vh'}),
                html.Br(),
                ], className='boxdiv'),
        # html.Div([
        #         dcc.Graph(id='tsne2d',
        #                   figure=tsne2d,
        #                   style={'display': 'inline-block', 'width': '90vh', 'height': '80vh'}),
        #         dcc.Graph(id='umap2d',
        #                   figure=umap2d,
        #                   style={'display': 'inline-block', 'width': '90vh', 'height': '80vh'}),
        # ]),
        # html.Div([
        #         dcc.Graph(id='tse-3d',
        #                   figure=tsne3d,
        #                   style={'display': 'inline-block', 'width': '90vh', 'height': '80vh'}),
        #         dcc.Graph(id='umap-3d',
        #                   figure=umap3d,
        #                   style={'display': 'inline-block', 'width': '90vh', 'height': '80vh'}),
        # ]),
        html.Div([
                html.H4('Password embedding visualization', style={'font-family': 'sans-serif'}),
                html.P('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
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
                             {'label': 'topics', 'value': 'label'},
                             {'label': 'zxcvbn score', 'value': 'zxcvbn'},
                             {'label': 'password composition', 'value': 'category'},
                         ],
                         style={'verticalAlign': 'middle', 'display': 'inline-block', 'width': '33%', 'font-family': 'sans-serif'}
                         ),
                dcc.Graph(id='interactive',
                          style={'display': 'inline-block', 'width': '150vh', 'height': '100vh', 'font-family': 'sans-serif'})
        ], className='boxdiv'),
        # html.Div([
        #         dcc.Dropdown(id='select-num-clusters',
        #                 options=[
        #                      {'label': '8', 'value': '8'},
        #                      {'label': '12', 'value': '12'},
        #                      {'label': '16', 'value': '16'},
        #                      {'label': 'Manual', 'value': 'manual'}
        #                  ],
        #                  value=8,
        #                  style={'display': 'inline-block','width': '33%'}
        #                  ),
        #         dcc.Graph(id='interactive-2',
        #                   style={'display': 'inline-block', 'width': '150vh', 'height': '100vh'})
        # ]),
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
                 color_discrete_sequence=px.colors.qualitative.T10,
                 )
    # fig.update_layout(yaxis_title='count')
    return fig


@app.callback(
    Output("zxcvbn-chart-2", "figure"),
    [Input(component_id='select-zxcvbn-score', component_property='value')]
)
def update_zxcvbn_2(score):
    frame2 = df.copy()
    frame2 = frame2.groupby(['zxcvbn', 'number_of_symbols']).count().reset_index()
    frame2 = frame2[['zxcvbn', 'number_of_symbols', 'frequency']]
    frame2['log'] = np.log(1+frame2['frequency'])
    frame2 = frame2[frame2.zxcvbn == score]

    fig = px.bar(data_frame=frame2,
                 x='number_of_symbols',
                 y='log',
                 color_discrete_sequence=px.colors.qualitative.T10,
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
                 color_discrete_sequence=px.colors.qualitative.T10,
                 )
    # fig.update_layout(yaxis_title='count')
    return fig2


@app.callback(
    Output('interactive', 'figure'),
    Input('select-column', 'value'),
    Input('select-embedding', 'value'),
)
def interactive_plot(col, map):
    if map == 'umap':
        frame = umap2.copy()
    elif map == 'tsne':
        frame = tsne2.copy()

    #frame['zxcvbn'] = frame['zxcvbn'].astype('string')
    int_fig = px.scatter(data_frame=frame , x='x', y='y', color=col,
                         #color_discrete_sequence=px.colors.qualitative.Prism,
                         hover_data=['password'])
    return int_fig

# @app.callback(
#     Output('interactive-2', 'figure'),
#     Input('select-num-clusters', 'value'),
# )
# def interactive_2_plot(clus):
#
#     frame = pd.read_csv('../data/data2use/Embedding/red_100_'+ str(clus) +'_umap_2.csv')
#
#     frame['label'] = frame['label'].astype('str')
#
#     #frame['zxcvbn'] = frame['zxcvbn'].astype('string')
#     int2_fig = px.scatter(data_frame=frame , x='x', y='y', color='label',
#                          #color_discrete_sequence=px.colors.qualitative.Alphabet,
#                          hover_data=['password'])
#     return int2_fig


if __name__ == "__main__":
    app.run_server(debug=True)