import os
from WordlGame import WordlGame

words = []
with open("tenKWords.txt") as line:
    words += line.read().split('\n')
words = words[:-1]

env = WordlGame(words, 5, 3)
env.generate_word()
inPlay = True
while inPlay:
    attempt = input("Attempt: ")
    output, done = env.step(attempt)
    if done != 0:
        inPlay = False


# test game
