import random


class Dice(object):

    def __init__(self, maxValue, minValue, currentValue):
        self.__maxValue = maxValue
        self.__minValue = minValue
        self.__currentValue = currentValue

    def getMaxValue(self):
        return self.__maxValue

    def getMinValue(self):
        return self.__minValue

    def roll(self):
        return random.randint(self.__minValue, self.__maxValue + 1)
