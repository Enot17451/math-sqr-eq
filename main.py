import enum
from random import *

class SignStatus(enum.Enum):
    fullSigns = 2
    onlyMinus = 1
    noSign = 0

class Number:
    def __init__(self,signStatus = SignStatus.fullSigns):
        self.n = randint(1,20)
        self.signStatus = signStatus
        self.sign = choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"])

    def __str__(self):
        if self.signStatus == SignStatus.fullSigns:
            return f"{self.sign}{self.n}"
        elif self.signStatus == SignStatus.onlyMinus:
            if self.sign == "-":
                return f"{self.sign}{self.n}"
            else:
                return f"{self.n}"
        else:
            return f"{self.n}"

class SqEq:
    def __init__(self):
        self.a = Number(SignStatus.onlyMinus)
        self.b = Number()
        self.c = Number()

    def __str__(self):
        return f"{self.a}x²{self.b}x{self.c}=0"


n = 20
for x in range(n):
    s = SqEq()
    print(s)
