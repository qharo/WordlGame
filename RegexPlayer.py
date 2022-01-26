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
        self.backupWords = self.words
        #self.words = list(filter(lambda v: re.match(".[h]", v), words))
        #self._outputify()
    
    def reset(self): self.words = self.backupWords

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
            #print(len(self.words))
            if raw[char][1] == 1:
                #print(f" RAW CHAR IS {raw[char][0]}")
                self.words = [word for word in self.words if raw[char][0] in word]
            elif raw[char][1] == 2:
                pass
                self.words = list(filter(lambda x: x[char] == raw[char][0], self.words))
            else:
                self.words = [word for word in self.words if raw[char][0] not in word]
        print("Options are: ")
        self._outputify()
        #print(f"Your next guess must be: {self.words[random.randint(0, len(self.words))]}")



env = WordlGame(words, 5, 6)
player = RegexPlayer(words, 5)
env.generate_word()
inPlay = True
manual = input("Enter M for Manual, A for auto: ")
while inPlay:
    attempt = input("Attempt: ")
    output = []
    if manual == 'A':
        output, done = env.step(attempt)
    elif manual == 'M':
        done = input("Done: ")
        result = input("Enter coded result: ")
        for char in range(len(attempt)):
            #result = input(char + ': ')
            output.append((attempt[char], int(result[char])))
    print(output)
    if int(done) != 0:
        print("comes here")
        inPlay = False
    else:
        player.guess(output)
# [('b', -1), ('u', -1), ('l', -1), ('g', -1), ('e', 0)]

# test game
