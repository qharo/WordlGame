import os
from WordlGame import WordlGame
import re

words = []
with open("tenKWords.txt") as line:
    words += line.read().split('\n')
words = words[:-1]

class RegexPlayer:
    def __init__(self, words, length):
        #self.words = list(filter(lambda v: re.match('\w{' + str(length) + '}', v), words))
        self.words = list(filter(lambda v: re.match(r'.*[a][a]*', v), words))
        self._outputify()
    
    def _outputify(self):
        print(self.words)
        print(f"Number of words: {len(self.words)}")

    def guess(self, raw):
        contains = []
        exact = []
        for char in raw:
            if char[1] == 0:
                contains.append('*')




env = WordlGame(words, 5, 3)
player = RegexPlayer(words, 5)
env.generate_word()
inPlay = True
while inPlay:
    attempt = input("Attempt: ")
    output, done = env.step(attempt)
    if done != 0:
        inPlay = False
    else:
        player.guess(output)


# test game
