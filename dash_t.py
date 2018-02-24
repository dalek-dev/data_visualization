# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 14:43:47 2018

@author: vict
"""

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
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

if __name__ == '__main__':
    app.run_server(debug=True)
