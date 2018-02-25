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
    @app.callback(
            Output(component_id = 'output_graph', component_property = 'children'),
            [Input(component_id = 'input', component_property = 'value')]
            )
    
    def update_graph(input_data):
        
        start = dt.datetime(2015, 1, 1)
        end = dt.datetime.now()
        df =  web.DataReader(input_data, 'google', start, end)
        
        return dcc.Graph(
                    id='ex1-graph',
                            figure={
                                    'data': [
                                            { 'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data},
                                            
                                            ],
                                    'layout': {                                        
                                            'title': input_data 
                                            }
                                    })
    
    
    if __name__ == '__main__':
        app.run_server(debug=True)
    
    
