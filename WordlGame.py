import random
from selectors import EpollSelector
import pandas as pd

words = []
with open("english2.txt") as line:
    words += line.read().split('\n')


class WordlGame:
    # gets list of words and filters for length
    def __init__(self, words, length, chances):
        print(f"{''.join(['-']*35)}\n\tWELCOME TO WORDL!\n{''.join(['-']*35)}")
        print(f"     Length of the world: {length}\n     Number of attempts: {chances}\n{''.join(['/']*35)}\n")
        self.numChances = chances
        self.chance = self.numChances
        self.words = [x for x in words if len(x) == length]
        self.length = length
    
    #randomly selects word
    def generate_word(self): self.choice = self.words[random.randint(0, len(self.words))]
    
    #outputs
    def _outputify(self, raw):
        output = ''
        for char in raw:
            letter = "_" if char[1] == -1 else char[0].lower() if char[1] == 0 else char[0].upper()
            output += letter + ' '
        print("Output: " + output + '\n')

    def _verifyAnswer(self, ans):
        if len(ans) == self.length:
            return True
        else:
            print("Not the right length, try again!")
            return False
        
    def _evaluate(self, answer):
        raw = []
        choice = self.choice
        for char in range(len(answer)):
            if answer[char] not in choice:
                raw.append((answer[char], 0))
            elif answer[char] == self.choice[char]:
                raw.append((answer[char], 2))
            else:
                raw.append((answer[char], 1))
        self.chance -= 1
        self._outputify(raw)
        return raw

    def step(self, answer):
        answer = answer.lower().strip()
        raw = []

        if self.chance == 0:
            print(f"Game has ended! The word was {self.choice}")
            return None, 1
        elif self._verifyAnswer(answer):
            if answer == self.choice:
                print("You won!")
                return None, 1
            raw = self._evaluate(answer)
            return raw, 0
        else:
            return raw, -1