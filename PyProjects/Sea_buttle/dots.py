class Dot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
class Ship:
    def __init__(self, head, direction, length):
        self.head = head
        self.direction = direction
        self.length = length
        self.hp = length

    @property
    def dots(self):
        ship_cells = []
        for i in range(self.length):
            new_x, new_y = self.head.x, self.head.y
            if self.direction == 1:
                new_x += i
            elif self.direction == 2:
                new_y += i
            ship_cells.append(Dot(new_x, new_y))
        return ship_cells