#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:02:56 2021

@author: danielrichardson
"""

import nltk
import csv
from afinn import Afinn
import matplotlib.pyplot as plt

def afinn_sentiment(corpus):
    total = 0

    for i in range(len(corpus)):
        total += af.score(corpus[i])
        
    
    return total/len(corpus)


def vader_sentiment(corpus):
    # nltk.download('vader_lexicon')
    compounds = []
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    sid = SentimentIntensityAnalyzer()
    
    total = 0
    for tweet in corpus:
        total += sid.polarity_scores(tweet)['compound']
        compounds.append(sid.polarity_scores(tweet)['compound'])
    
    

    # An "interface" to matplotlib.axes.Axes.hist() method
    n, bins, patches = plt.hist(x=compounds, bins='auto', color='#0504aa',
                                alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Vader Compound Sentiment Score')
    plt.ylabel('Frequency')
    plt.title('Tweets about Kirsten Synema up to 3/5')
    # plt.text(23, 45, r'$\mu=15, b=3$')
    plt.show()
    
    return total/len(corpus)



af = Afinn()

sinema_before_corpus = []

with open('sinemabeforetweets.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
           sinema_before_corpus.append(row[3])
        line_count += 1

# tokenizer = nltk.tokenize.WhitespaceTokenizer()


print(afinn_sentiment(sinema_before_corpus))
print(vader_sentiment(sinema_before_corpus))


    