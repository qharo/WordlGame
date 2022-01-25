import os
from WordlGame import WordlGame
import re
import random

words = []
with open("tenKWords.txt") as line:
    words += line.read().split('\n')
words = words[:-1]

class RegexPlayer:
    def __init__(self, words, length):
        self.words = list(filter(lambda v: re.match(r'^\w\w\w\w\w$', v), words))
        #self.words = list(filter(lambda v: re.match(".[h]", v), words))
        self._outputify()
    
    def _outputify(self):
        print(self.words)
        print(f"Number of words: {len(self.words)}")

    # def _regexify(self, regexs):
    #     for r in regexs:
    #         self.words = list(filter(lambda v: re.match(r, v), self.words))
    #     print(self.words)

    # def guess(self, raw):
    #     regexs = []
    #     for char in range(len(raw)):
    #         print(char)
    #         if raw[char][1] == 0:
    #             for i in range(len(raw)):
    #                 if i != char:
    #                     temp = ['\w', '\w', '\w', '\w', '\w']
    #                     temp[i] = raw[char][0]
    #                     #regexs.append(''.join(temp))
    #             #regexs.append('[' + raw[char][0] + ']')
    #         elif raw[char][1] == 1:
    #             temp = ['\w', '\w', '\w', '\w', '\w']
    #             temp[char] = raw[char][0]
    #             regexs.append(''.join(temp))
    #         else:
    #             regexs.append("^((?!" + raw[char][0] + ").)*$")
    #     print(regexs)
    #     self._regexify(regexs)
    #     #print(self.words[0])

    def guess(self, raw):
        for char in range(len(raw)):
            print(raw[char])
            if raw[char][1] == 0:
                self.words = [word for word in self.words if raw[char][0] in word]
            elif raw[char][1] == 1:
                self.words = list(filter(lambda x: x[char] == raw[char][0], self.words))
            else:
                self.words = [word for word in self.words if raw[char][0] not in word]
        self._outputify()
        #print(f"Your next guess must be: {self.words[random.randint(0, len(self.words))]}")



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
