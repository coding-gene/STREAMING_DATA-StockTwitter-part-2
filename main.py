# https://github.com/anubhavanand12qw/STOCK-PRICE-PREDICTION-USING-TWITTER-SENTIMENT-ANALYSIS/blob/master/STOCK%20PREDICTION%20USING%20TWITTER%20SENTIMENT%20ANALYSIS%20PROJECT%20(FINAL)%20-%20Updated.ipynb
# https://github.com/talaikis/StockTalk3
# https://stackoverflow.com/questions/63589249/plotly-dash-display-real-time-data-in-smooth-animation
# https://dash.plotly.com/live-updates
# https://www.youtube.com/watch?v=hSPmj7mK6ng
# https://www.youtube.com/watch?v=psvU4zwO3Ao
# pipenv lock -r > requirements.txt
# https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
from data.dataframe import DataForPlotting
import pandas as pd
import logging
import time
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np


pd.set_option('display.max_rows', 40)
pd.set_option('display.max_columns', 40)
pd.set_option('display.width', 200)
pd.set_option('display.max_colwidth', 300)

logging.basicConfig(filename='logs.txt',
                    filemode='a',
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

# noinspection PyBroadException
try:
    external_stylesheets = ['https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    data = DataForPlotting()
    df = data.get_df()

    app.layout = html.Div(style={'backgroundColor': 'blue'},
                          children=[
        html.H1('STOCK SENTIMENT ANALYSIS USING TWITTER DATA',
                style={'text-align': 'center',
                       'color': 'white',
                       'backgroundColor': 'black',
                       'font': 'bold'}),
        html.P('Visualising Stock And Twitter Data',
               style={'text-align': 'center',
                       'color': 'white',
                       'backgroundColor': 'blue',
                       'font': 'bold'}),
        dcc.Graph(id='sentiment_analysis', style={'color': 'blue'}),
        dcc.Slider(
            id='month-slider',
            min=df['month'].min(),
            max=df['month'].max(),
            value=df['month'].min(),
            marks={str(month): str(month) for month in df['month'].unique()},
            step=None)
    ])

    @app.callback(
        Output(component_id='sentiment_analysis', component_property='figure'),
        Input(component_id='month-slider', component_property='value'))
    def update_graph(selected_day):
        filtered_df = df[df.month == selected_day]
        line_fig = px.scatter(data_frame=filtered_df,
                              x='price', y='polarity',
                              size='subjectivity',
                              color='change_percentage',
                              log_x=True,
                              size_max=55)
        line_fig.update_layout(transition_duration=500)
        return line_fig

    app.run_server(debug=True)
except Exception:
    logging.exception('An error occurred during job performing:')
