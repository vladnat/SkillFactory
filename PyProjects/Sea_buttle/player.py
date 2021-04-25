from random import randint

from dots import Dot
from exceptions import WrongValueException, Error

class Player:
    def __init__(self, board, opp):
        self.board = board
        self.opp = opp

    def ask(self):
        pass

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.opp.hit(target)
                return repeat
            except Error as e:
                print(e)


class AI(Player):
    def ask(self):
        cords = Dot(randint(1, 10), randint(1, 10))
        print(f"AI shoots {cords.x}, {cords.y}")
        return cords


class User(Player):
    def ask(self):
        while True:
            cords = input("Shoot!!!: ").split()
            if len(cords) != 2:
                raise WrongValueException()
            x, y = cords
            if not (x.isdigit()) or not (y.isdigit()):
                raise WrongValueException()
            return Dot(int(x), int(y))