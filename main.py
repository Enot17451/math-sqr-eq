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

class SqEq:
    def __init__(self):
        self.a = Number(False)
        self.b = Number()
        self.c = Number()

    def __str__(self):
        return f"{self.a}x²{self.b}x{self.c}=0"


n = 20
for x in range(n):
    s = SqEq()
    print(s)
