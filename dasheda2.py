import pandas as pd
import plotly.graph_objects as go
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
```python
app.layout = html.Div(children=[
  
                            html.H1(`Flight Delay Time Statistics`, style={textAlign='right', color=503D36, font-size=30}),
                            html.Div(["Input Year: ", dcc.Input(id='...TODO2...', value='...TODO2...', type='...TODO2...', style={'...TODO2...'}),], style={'font-size': 30}),
                            html.Br(),
                            html.Br(),
                          
                            html.Div([
                                        html.Div('...TODO3...'),
                                        html.Div('...TODO3...')
                                ], style={'display': 'flex'}),
    
                                html.Div([
                                        html.Div('...TODO3...'),
                                        html.Div('...TODO3...')
                                ], style={'display': 'flex'}),
                                
                                html.Div('...TODO3...', style={'width':'65%'})
                       
                                ])

# add callback decorator
@app.callback( [
               Output(...TODO4...),
               Output(...TODO4...),
               Output(...TODO4...),
               Output(...TODO4...),
               Output(...TODO4...)
               ],
               Input(...TODO4...))
               
# Add computation to callback function and return graph
def get_graph(entered_year):
    
    # Compute required information for creating graph from the data
    ...TODO5..., ...TODO5..., ...TODO5..., ...TODO5..., ...TODO5... = compute_info(airline_data, entered_year)
            
    # Create graph
    carrier_fig = px.line(...TODO6..., x='...TOTO6...', y='...TOTO6...', color='...TOTO6...', title='...TOTO6...')
    weather_fig = px.line(...TODO6..., x='...TOTO6...', y='...TOTO6...', color='...TOTO6...', title='...TOTO6...')
    nas_fig = px.line(...TODO6..., x='...TOTO6...', y='...TOTO6...', color='...TOTO6...', title='...TOTO6...')
    sec_fig = px.line(...TODO6..., x='...TOTO6...', y='...TOTO6...', color='...TOTO6...', title='...TOTO6...')
    late_fig = px.line(...TODO6..., x='...TOTO6...', y='...TOTO6...', color='...TOTO6...', title='...TOTO6...')
            
    return[carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]


# Run the app
if __name__ == '__main__':
    app.run_server(mode='jupyterlab')
```
