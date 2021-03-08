import dash_grid
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq
#import pandas as pd
app = dash.Dash(__name__)

"""import plotly.express as px

df = px.data.iris() # iris is a pandas DataFrame
fig = px.scatter(df, x="sepal_width", y="sepal_length")
import plotly.graph_objs as go
fig1 = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
fig2 = px.pie(df, values='pop', names='country', title='Population of European continent')
fig3 = px.imshow([[1, 20, 30],
                 [20, 1, 60],
                 [30, 60, 1]])"""

positionlay=[{'w': 2, 'h': 1, 'x': 0, 'y': 0, 'i': 'status1', 'moved': False, 'static': False}, {'w': 2, 'h': 4, 'x': 0, 'y': 1, 'i': 'status2', 'moved': False, 'static': False}, {'w': 2, 'h': 1, 'x': 5, 'y': 0, 'i': 'my-multi-dynamic-dropdown', 'moved': False, 'static': False}, {'w': 2, 'h': 3, 'x': 0, 'y': 6, 'i': 'my-LED-display', 'moved': False, 'static': False}, {'w': 2, 'h': 3, 'x': 0, 'y': 9, 'i': 'my-LED-display1', 'moved': False, 'static': False}, {'w': 7, 'h': 1, 'x': 5, 'y': 12, 'i': 'example-graph', 'moved': False, 'static': False}, {'w': 5, 'h': 12, 'x': 0, 'y': 12, 'i': 'example-graph1', 'moved': False, 'static': False}, {'w': 5, 'h': 11, 'x': 7, 'y': 0, 'i': 'example-graph2', 'moved': False, 'static': False}, {'w': 5, 'h': 10, 'x': 2, 'y': 1, 'i': 'example-graph3', 'moved': False, 'static': False}, {'w': 1, 'h': 1, 'x': 0, 'y': 24, 'i': 'tabs-example', 'moved': False, 'static': False}, {'w': 1, 'h': 1, 'x': 0, 'y': 25, 'i': 'tabs-example-content', 'moved': False, 'static': False}]

"""app.layout = html.Div([
      daq.PowerButton(
        id='my-power-button',
        on=False
    ),
    html.Div(id='power-button-output'),
    dash_grid.DashGrid(
        id='syncdashboard',
        position = positionlay,
        editable=False,
        children=[
             html.P(id = "status1",children=["init-status"] ),
             html.P(id = "status2",children=["init-power"] ),
             dcc.Dropdown(
         id="my-multi-dynamic-dropdown",
         options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
        {'label': 'San Fraisco', 'value': 'SF1'},
        {'label': 'San Francisco', 'value': 'SF2'},
    ],
    value='MTL',
    clearable=False
),  
             daq.LEDDisplay(
               id='my-LED-display',
               label="Default",
               value=6
             ),
             daq.LEDDisplay(
               id='my-LED-display1',
               label="Default",
               value=16
             ),
             dcc.Graph(
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
              ),
              dcc.Tabs(id='tabs-example', value='tab-1', children=[
                   dcc.Tab(label='Tab one', value='tab-1'),
                   dcc.Tab(label='Tab two', value='tab-2'),
               ]),
               html.Div(id='tabs-example-content')
             
]
    ),
    html.Div(id='output')
])"""

app.layout = html.Div([
    daq.PowerButton(
                id='my-power-button',
                on=False
             ),
    html.Div(id='power-button-output'),
    dash_grid.DashGrid(
        id='syncdashboard',
        position = positionlay,
        editable=False,
        children=[
             html.P(id = "status1",children=["init-status"] ),
         #    html.P(id = "statue2",children=["init-status"] ),
        ]
    )
    ])
"""@app.callback(Output("output", "children"),[Input("syncdashboard", "position")] )
def render_content(input_value):
     positionlay=input_value
     return 'Output: {}'.format(input_value)

@app.callback(Output('tabs-example-content', 'children'),
              Input('tabs-example', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            html.H3('Tab content 1')
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('Tab content 2')
        ])"""

@app.callback(Output('power-button-output', 'children'),[Input('my-power-button', 'on'),Input("syncdashboard", "editable")])
def update_output(on,value):
    return 'The button is {}.'.format(value)



@app.callback(Output("syncdashboard", "editable"),[Input('my-power-button', 'on')] )
def render_content(enable):
       if enable == True:
          return True
       else:
          return False

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
