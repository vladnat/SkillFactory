from random import randint

from field import Field
from dots import Ship, Dot
from player import AI, User
from exceptions import CannotPlaceShip

class Game:
    def __init__(self, size=10):
        self.size = size
        board_1 = self.random_board()
        board_2 = self.random_board()
        board_2.hid = True
        self.user = User(board_1, board_2)
        self.ai = AI(board_2, board_1)

    def create_ships(self):
        ships = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
        board = Field(size=self.size)
        a = 0
        for i in ships:
            while True:
                a += 1
                if a > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), randint(1, 2), i)
                try:
                    board.add_ship(ship)
                    break
                except CannotPlaceShip:
                    pass
        board.check()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.create_ships()
        return board

    @staticmethod
    def logo():
        print("___________________")
        print("|   SEA  BUTTLE   |")
        print("|#################|")
        print("|   Use 1 to 10   |")
        print("|_____to shoot____|")    

    def loop(self):
        turns = 0
        while True:

            print("User:")
            self.user.board.show()
            print("#" * 22)
            print("AI:")
            self.ai.board.show()
            if turns % 2 == 0:
                print("#" * 23)
                print("Make a turn")
                repeat = self.user.move()
            else:
                print("#" * 23)
                print("AI makes a turn")
                repeat = self.ai.move()
            if repeat:
                turns -= 1
            if self.ai.board.alive == 0:
                print("#" * 23)
                print("You win!")
                break
            elif self.user.board.alive == 0:
                print("-" * 23)
                print("AI wins!")
                break
            turns += 1

    def start(self):
        self.logo()
        self.loop()

game = Game()
game.start()