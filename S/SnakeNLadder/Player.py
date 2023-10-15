class Player(object):
    def __init__(self, name):
        self.__name = name
        self.__position = 0
        self.__won = False

    def getName(self):
        return self.__name

    def getPosition(self):
        return self.__position

    def getWon(self):
        return self.__won

    def setPosition(self, position):
        self.__position = position

    def setWon(self, won):
        self.__won = won
