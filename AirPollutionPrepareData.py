# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 17:23:16 2018

@author: Vegard
"""

from pandas import read_csv
from datetime import datetime

def parse(x):
    return datetime.strptime(x,'%Y %m %d %H')
dataset = read_csv('raw.csv', parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True) #Remove index
dataset.columns = ['pollution', 'dew', 'temp','press','wnd_dir','wnd_spd','snow','rain']
dataset.index.name = 'date'
dataset['pollution'].fillna(0,inplace=True)
dataset = dataset[24:]
print(dataset.head(5))
dataset.to_csv('pollution.csv')


