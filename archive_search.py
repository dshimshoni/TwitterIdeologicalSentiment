#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 16:31:06 2021

@author: danielrichardson
"""

import tweepy 
import json
import re

_consumer_key = 'TmpG43n33c4ZeG2DluFqU2B5E'
_consumer_secret = 'Ta47kggFdk4N3N0DKzfc8duGaBEdTR6YnEjonLrntH46qhHArP'

_access_token = '881921096529924098-UhnDNrabRqf36NDbVcnU3F8BM7oVxDt'
_access_token_secret= 'Kp5x6TMTFEdhkN4SEvDDCxq0YYQprBH2PuR6NykJlCE0L'

auth = tweepy.OAuthHandler(_consumer_key, _consumer_secret)
auth.set_access_token(_access_token, _access_token_secret)

api = tweepy.API(auth)


#Give 10 tweets that mention socialism from February 1 2020 to March 1 2020
results = api.search_full_archive('development',
                                  'socialism',
                                  fromDate = '202002010000',
                                  toDate = '202002010010',
                                  maxResults = 1)

total = 1

for tweet in results:
    if(tweet.lang == 'en'):
        
        #Maybe is:retweet works here??
        if(not re.search('RT +.', tweet.text)):
            
            #Didn't test this yet, may eliminate too many tweets.
            # if('USA' in tweet.user.location):
                print(total,tweet.text,tweet.user.location)
                total += 1
            
print(total - 1)
    
    