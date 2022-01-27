import os
from WordlGame import WordlGame
import re
import random

# words = []
# with open("english2.txt") as line:
#     words += line.read().split('\n')
# words = words[:-1]

words = []
with open("english2.txt") as line:
    words += line.read().split('\n')

class StrPlayer:
    def __init__(self, words, length):
        self.words = list(filter(lambda v: re.match(r'^\w\w\w\w\w$', v), words))

    def _outputify(self):
        print(self.words)
        print(f"Number of words: {len(self.words)}\n")

    def guess(self, raw):
        for char in range(len(raw)):
            if raw[char][1] == 1:
                self.words = [word for word in self.words if raw[char][0] in word]
                self.words = list(filter(lambda x: x[char] != raw[char][0], self.words))
            elif raw[char][1] == 2:
                self.words = list(filter(lambda x: x[char] == raw[char][0], self.words))
            else:
                self.words = [word for word in self.words if raw[char][0] not in word]
        print("\nOptions are: ")
        self._outputify()



inPlay = True
manual = 'R'
while inPlay:
    if manual == 'R':
        env = WordlGame(words, 5, 6)
        env.generate_word()
        player = StrPlayer(words, 5)
        manual = input("Enter M for Manual, A for auto, R to Restart, Q to Quit: ")
    
    elif manual == 'Q':
        inPlay = False

    else:
        attempt = input("Attempt: ")
        output = []
        if attempt == '-1':
            manual = 'R'
        else:
            if manual == 'A':
                output, done = env.step(attempt)
            elif manual == 'M':
                result = input("Enter coded result: ")
                for char in range(len(attempt)):
                    output.append((attempt[char], int(result[char])))
            player.guess(output)
