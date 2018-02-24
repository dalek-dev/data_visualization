# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:43:47 2018

@author: vict
"""

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

import pandas_datareader.data as web
import datetime as dt



start = dt.datetime(2015, 1, 1)
end = dt.datetime.now() 

stock = 'TSLA'

df =  web.DataReader(stock, 'google', start, end)

app = dash.Dash()   

app.layout = html.Div(children = [
        html.H1('Dash Data'),
        html.Div(children='''
            Graph:        
        '''),
            dcc.Input(id = 'input', value = '', type = 'text'),
            html.Div('output-graph')
])


"""
        dcc.Graph(
                id='ex1',
                        figure={
                                'data': [
                                        { 'x': df.index, 'y': df.Close, 'type': 'line', 'name': stock},
                                        
                                        ],
                                'layout': {                                        'title': stock
                                        }
                                })
"""
@app.callback(
        Output(component_id = 'output_graph', component_property = 'children'),
        [Input(component_id = 'input', component_property = 'value')]
        )

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
"""
if __name__ == '__main__':
    app.run_server(debug=True)
