#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 15:47:16 2021

@author: danielrichardson
"""
import pandas as pd
import numpy as np


df = pd.read_csv('data_with_scores.csv')
df.rename(columns={'after_vote': 'Time'},inplace=True)

df['Time'] = np.where(df['Time'] == 0, 'Week Before March 5 Vote','Week of March 5 and After')

df.groupby(['senator','Time']).mean()['vader_scores'].unstack().plot(
    xlabel = 'Senator', 
    ylabel = 'Average Vader Senitment Score', 
    kind = 'bar',
    title = 'Twitter Sentiment of Senators Before and After Voting "No" on Minimum Wage Increase')

df.groupby(['senator','Time']).mean()['afinn_scores'].unstack().plot(
    xlabel = 'Senator', 
    ylabel = 'Average Afinn Senitment Score', 
    kind = 'bar',
    title = 'Twitter Sentiment of Senators Before and After Voting "No" on Minimum Wage Increase')

