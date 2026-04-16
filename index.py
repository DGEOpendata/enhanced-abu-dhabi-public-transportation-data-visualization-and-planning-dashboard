python
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load the dataset
transportation_data = pd.read_csv('Abu_Dhabi_Public_Transportation_Metrics.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Abu Dhabi Public Transportation Dashboard"),
    dcc.Dropdown(
        id='route-dropdown',
        options=[{'label': route, 'value': route} for route in transportation_data['Route_ID'].unique()],
        placeholder="Select a bus route"
    ),
    dcc.Graph(id='ridership-graph'),
    dcc.Graph(id='wait-time-graph')
])

# Callbacks for interactive graphs
@app.callback(
    Output('ridership-graph', 'figure'),
    [Input('route-dropdown', 'value')]
)
def update_ridership_graph(selected_route):
    if selected_route:
        filtered_data = transportation_data[transportation_data['Route_ID'] == selected_route]
        fig = px.line(filtered_data, x='Date', y='Ridership', title=f'Ridership for Route {selected_route}')
        return fig
    return {}

@app.callback(
    Output('wait-time-graph', 'figure'),
    [Input('route-dropdown', 'value')]
)
def update_wait_time_graph(selected_route):
    if selected_route:
        filtered_data = transportation_data[transportation_data['Route_ID'] == selected_route]
        fig = px.bar(filtered_data, x='Date', y='Average_Wait_Time', title=f'Average Wait Time for Route {selected_route}')
        return fig
    return {}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
