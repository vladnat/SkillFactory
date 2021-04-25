from exceptions import BoardOutException, UsedCellException, WrongValueException, CannotPlaceShip
from dots import Dot

class Field:
    def __init__(self, hid=False, size=10):
        self.size = size
        self.hid = hid
        self.alive = 10
        self.map = [['  ', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'],
                    ['1 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['2 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['3 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['4 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['5 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['6 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['7 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['8 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['9 ', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
                    ['10', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
                    ]

        self.used = []
        self.ships = []

    @staticmethod
    def outside(i):
        return False if (i.x in range(1, 11) and i.y in range(1, 11)) else True

    def add_ship(self, ship):

        for cell in ship.dots:
            if self.outside(cell) or cell in self.used:
                raise CannotPlaceShip()
        for cell in ship.dots:
            self.map[cell.x][cell.y] = "■"
            self.used.append(cell)
        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, cnt=False):
        contour_ = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1), (0, 0), (0, 1),
                    (1, -1), (1, 0), (1, 1)]
        for i in ship.dots:
            for a, b in contour_:
                c = Dot(i.x + a, i.y + b)
                if not (self.outside(c)) and c not in self.used:
                    if cnt:
                        self.map[c.x][c.y] = "0"
                    self.used.append(c)

    def show(self):
        for i in range(1):
            for j in range(11):
                if self.hid:
                    for a in range(11):
                        for b in range(11):
                            if self.map[a][b] == "■":
                                self.map[a][b] = "."
                print("|".join(self.map[j]) + "|")

    def hit(self, s):
        if self.outside(s):
            raise BoardOutException()
        if s in self.used:
            raise UsedCellException()
        self.used.append(s)
        for ship in self.ships:
            if s in ship.dots:
                ship.hp -= 1
                self.map[s.x][s.y] = "X"
                if ship.hp == 0:
                    self.alive -= 1
                    self.contour(ship, cnt=True)
                    print(f"Ship destroyed! {self.alive} ships left!")
                    print()
                    return True
                else:
                    print("Ship damaged!")
                    print()
                    return True

        self.map[s.x][s.y] = "0"
        print("Shot missed!")
        return False

    def check(self):
        self.used = []