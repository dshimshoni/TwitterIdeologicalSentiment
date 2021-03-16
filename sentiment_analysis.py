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
    
    for tweet in corpus['cleaned_tweets']:
        af_scores.append(af.score(tweet))

    return af_scores

def vader_sentiment(corpus):
    # You'll need to run this if you've never downloaded the 
    # vader lexicon before
    # nltk.download('vader_lexicon')
    
    compounds = []
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    sid = SentimentIntensityAnalyzer()
    
    # for token_list in corpus['tokens']:
    #     score = 0
    #     cleaned_tweet = ''
    #     for token in token_list:
    #         cleaned_tweet += token + ' '
    #     print(cleaned_tweet)
    #     score = sid.polarity_scores(cleaned_tweet)['compound']
        # compounds.append(score)
    
    for tweet in corpus['cleaned_tweets']:
        compounds.append(sid.polarity_scores(tweet)['compound'])
    
    return compounds


df = pd.read_csv('senator_tweets.csv')

tk = WhitespaceTokenizer()
tokens = []
cleaned_tweets = []
for tweet in df['text']:
    tweet_tokens = []
    cleaned_tweet = ''
    for token in tk.tokenize(tweet):
        if('@' not in token and 'http' not in token):
            #If we wanted this is where stop word removal
            #and other cleaning could happen
            
            tweet_tokens.append(token)
            cleaned_tweet += token + ' '
    tokens.append(tweet_tokens)
    cleaned_tweets.append(cleaned_tweet)
            
df['tokens'] = tokens
df['cleaned_tweets'] = cleaned_tweets
df['afinn_scores'] = afinn_sentiment(df)
df['vader_scores'] = vader_sentiment(df)

df.to_csv('data_with_scores.csv', index=False)
    

    