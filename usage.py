import dash_grid
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
import pandas as pd
app = dash.Dash(__name__)

import plotly.express as px

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
import plotly.graph_objs as go
fig1 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig2 = px.pie(df, values='pop', names='country', title='Population of European continent')
fig3 = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])

positionlay=[
  {
    "w": 2,
    "h": 4,
    "x": 0,
    "y": 0,
    "i": "0",
    "moved": False,
    "static": False
  },
  {
    "w": 2,
    "h": 4,
    "x": 2,
    "y": 0,
    "i": "1",
    "moved": False,
    "static": False
  },
  {
    "w": 2,
    "h": 5,
    "x": 4,
    "y": 0,
    "i": "2",
    "moved": False,
    "static": False
  },
  {
    "w": 2,
    "h": 5,
    "x": 8,
    "y": 0,
    "i": "3",
    "moved": False,
    "static": False
  }
]
app.layout = html.Div([
    dash_grid.DashGrid(
        id='syncdashboard',
        position = positionlay,
        children=[
             html.P(id = "status1",children=["init-status"] ),
             html.P(id = "status2",children=["init-power"] ),
             daq.LEDDisplay(
               id='my-LED-display',
               label="Default",
               value=6
             ),
             daq.LEDDisplay(
               id='my-LED-display1',
               label="Default",
               value=16
             )
             
]
    ),
    html.Div(id='output')
])

"""dcc.Graph(
                id='example-graph',
                figure=fig
              ),
               dcc.Graph(
                id='example-graph1',
                figure=fig1
              ),
              dcc.Graph(
                id='example-graph2',
                figure=fig2
              ),
              dcc.Graph(
                id='example-graph3',
                figure=fig3
              )"""
if __name__ == '__main__':
    app.run_server(debug=True)
