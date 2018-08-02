# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 18:52:24 2018

@author: Dell
"""

import nltk
nltk.download('punkt')
from nltk.tokenize import  word_tokenize
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))
