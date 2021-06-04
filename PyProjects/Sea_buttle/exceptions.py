class Error(Exception):
    pass

class BoardOutException(Error):
    def __str__(self):
        return "Shot outside board!"


class UsedCellException(Error):
    def __str__(self):
        return "This cell already shot!"


class WrongValueException(Error):
    def __str__(self):
        return "Invalid coordinates specified!"


class CannotPlaceShip(Error):
    def __str__(self):
        return "No suitable space for ship!"