from random import *

class Number:
    def __init__(self,fullSign = True):
        self.n = randint(1,10)
        self.fullSign = fullSign
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        if self.fullSign:
            return f"{self.sign}{self.n}"
        else:
            if self.sign == "-":
                return f"{self.sign}{self.n}"
            else:
                return f"{self.n}"

class Var:
    def __init__(self,fullSign = True,letter="x"):
        self.n = randint(1,10)
        self.letter = letter
        self.fullSign = fullSign
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        if self.fullSign:
            if self.n == 1:
                return f"{self.sign}{self.letter}"
            else:
                return f"{self.sign}{self.n}{self.letter}"
        else:
            if self.n == 1:
                return f"{self.letter}"
            else:
                return f"{self.n}{self.letter}"

class BracketsMultiply:
    def __init__(self):
        isFirstVar = choice([True,False,True,False,False,True,False,True,False,False,True,False,True,False,False])
        if isFirstVar:
            self.a = Var(False)
            self.b = Number(False)
            self.c = Number()
        else:
            self.a = Number(False)
            whichNumberIsVar = randint(1,3)
            if whichNumberIsVar == 1:
                self.b = Var(False)
                self.c = Number()
            elif whichNumberIsVar == 2:
                self.b = Number(False)
                self.c = Var()
            else:
                self.b = Var(False)
                self.c = Var()

    def __str__(self):
        return f"{self.a}({self.b}{self.c})"


n = 20
for x in range(n):
    s = BracketsMultiply()
    print(s)
