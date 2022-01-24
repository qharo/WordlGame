import random
import pandas as pd

words = []
with open("tenKWords.txt") as line:
    words += line.read().split('\n')
words = words[:-1]

class WordlGame:
    def __init__(self, words, length, chances):
        # gets list of words and filters for length
        print("----------------------------------\n\tWELCOME TO WORDL!")
        print("----------------------------------")
        print(f"     Length of the world: {length}\n     Number of attempts: {chances}")
        print("//////////////////////////////////\n")
        self.numChances = chances
        self.chance = self.numChances
        self.words = [x for x in words if len(x) == length]
        self.length = length
    
    #randomly selects word
    def generate_word(self): self.choice = self.words[random.randint(0, len(self.words))]
    #def generate_word(self): self.choice = "hello"
    
    def _outputify(self, raw):
        # outputs raw file as clean text
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
        for char in range(len(answer)):
            if answer[char] in self.choice:
                if answer[char] == self.choice[char]:
                    raw.append((answer[char], 1))
                else:
                    raw.append((answer[char], 0))
            else:
                raw.append((char, -1))
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



# game = WordlGame(words, 5, 3)
# game.generate_word()
# done = False
# game.step("yulle")
# while not done:
#     output, success = game.step("hello")
#     if success == 1: done = True
#     #print(output)