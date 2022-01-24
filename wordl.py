import pandas as pd
import os

#A = pd.read_csv("A.csv", encoding='iso-8859-1')
#print(A)

words = []

with open("tenKWords.txt") as line:
    words += line.read().split('\n')
    #print(words)

words = words[:-1]

print(words)