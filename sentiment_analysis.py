#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 10 21:02:56 2021

@author: danielrichardson
"""

import nltk
import csv
from afinn import Afinn

af = Afinn()

corpus = []

with open('sinemabeforetweets.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
           corpus.append(row[3])
        line_count += 1

tokenizer = nltk.tokenize.WhitespaceTokenizer()

total = 0

for i in range(len(corpus)):
    total += af.score(corpus[i])
    
print(total/700)
