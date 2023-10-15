class Board(object):

    def __init__(self, size):
        self.__size = size
        self.__start = 1
        self.__end = self.__start + size - 1

    def getSize(self):
        return self.__size

    def getStart(self):
        return self.__start

    def getEnd(self):
        return self.__end
