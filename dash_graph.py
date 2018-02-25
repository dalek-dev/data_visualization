# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 16:53:20 2018

@author: vict
"""

import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2018, 2, 8)

df =  web.DataReader('TSLA', 'google', start, end)

print(df.head())



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
