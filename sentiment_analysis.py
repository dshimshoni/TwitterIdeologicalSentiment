#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:02:56 2021

@author: danielrichardson
"""

from nltk.tokenize import WhitespaceTokenizer
import pandas as pd
from afinn import Afinn

def afinn_sentiment(corpus):
    af = Afinn()
    af_scores = []
    
    for token_list in corpus['tokens']:
        total = 0
        for token in token_list:
            total += af.score(token)
        af_scores.append(total)

    return af_scores


def vader_sentiment(corpus):
    # You'll need to run this if you've never downloaded the 
    # vader lexicon before
    # nltk.download('vader_lexicon')
    
    compounds = []
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    sid = SentimentIntensityAnalyzer()
    
    for token_list in corpus['tokens']:
        total = 0
        for token in token_list:
            total += sid.polarity_scores(token)['compound']
        compounds.append(total)
    
    return compounds


df = pd.read_csv('senator_tweets.csv')

#Add tokens as a df column

tk = WhitespaceTokenizer()
tokens = []
for tweet in df['text']:
    tweet_tokens = []
    for token in tk.tokenize(tweet):
        if('@' not in token and 'http' not in token):
            #If we wanted this is where stop word removal
            #and other cleaning could happen
            
            tweet_tokens.append(token)
    tokens.append(tweet_tokens)
            
df['tokens'] = tokens
df['af_scores'] = afinn_sentiment(df)
df['vader_scores'] = vader_sentiment(df)

df.to_csv('data_with_scores.csv', index=False)
    
    
    