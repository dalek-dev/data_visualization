# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:43:47 2018

@author: vict
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()   
"""
app.layout = html.Div(children = [
        html.H1('Dash t'),
        dcc.Graph(id='ex1',
                        figure={
                                'data': [
                                        {'x':[1,2,3,4,5], 'y': [5,6,7,1,2], 'type': 'line', 'name': 'badges'},
                                        {'x':[1,2,3,4,5], 'y': [8,3,2,1,5], 'type': 'bar', 'name': 'motebike'}
                                        ],
                                'layout': {
                                        'title': 'Test Dash'
                                        }
                                })
        ])
"""
app.layout = html.Div(children=[
        dcc.Input(id = 'input', value = 'Ingrese un dato', type = 'text'),
        html.Div(id = 'output') 
        ])

@app.callback(
        Output(component_id = 'output', component_property = 'children'),
        [Input(component_id = 'input', component_property = 'value')])

def update_value(input_data):
    try:
        #return "Input: {}".format(input_data)
        return str(float(input_data)**2)
    except:
        return "Oh Por Dios Un Error D:"

if __name__ == '__main__':
    app.run_server(debug=True)
