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
