import random

from Snake import Snake
from Ladder import Ladder
from Board import Board
from Dice import Dice
from collections import deque


class Game(object):

    def __init__(self, noOfLadders, noOfSnakes, boardSize):
        self.__noOfLadders = noOfLadders
        self.__noOfSnakes = noOfSnakes
        self.__players = deque()
        self.__snakes = list()
        self.__ladders = list()
        self.__board = Board(boardSize)
        self.__dice = Dice(6, 1, 2)
        self.__initBoard()
        self.__ranking = list()

    def getNoOfLadders(self):
        return self.__noOfLadders

    def getNoOfSnakes(self):
        return self.__noOfSnakes

    def getPlayers(self):
        return self.__players

    def __initBoard(self):
        sl = set()
        board = self.getBoard()
        for i in range(self.getNoOfSnakes()):
            while (True):
                snakeStart = random.randint(board.getStart(), board.getSize())
                snakeEnd = random.randint(board.getStart(), board.getSize())
                if (snakeEnd >= snakeStart):
                    continue
                startEndPair = str(snakeStart) + str(snakeEnd)
                if startEndPair not in sl:
                    snake = Snake(snakeStart, snakeEnd)
                    self.getSnakes().append(snake)
                    break

        for i in range(self.getNoOfLadders()):
            while (True):
                ladderStart = random.randint(board.getStart(), board.getSize())
                ladderEnd = random.randint(board.getStart(), board.getSize())
                if (ladderEnd >= ladderStart):
                    continue
                endStartPair = str(ladderEnd) + str(ladderStart)
                if endStartPair not in sl:
                    ladder = Ladder(ladderStart, ladderEnd)
                    self.getLadders().append(ladder)
                    break

    def getBoard(self):
        return self.__board

    def getDice(self):
        return self.__dice

    def getSnakes(self):
        return self.__snakes

    def getLadders(self):
        return self.__ladders

    def addPlayer(self, player):
        self.__players.append(player)

    def playGame(self):
        while (True):
            player = self.__players.popleft()
            val = self.__dice.roll()
            newPosition = player.getPosition() + val
            if (newPosition > self.__board.getEnd()):
                player.setPosition(player.getPosition())
                self.__players.append(player)

            else:
                player.setPosition(self.__getNewPosition(newPosition))
                if (player.getPosition() == self.__board.getEnd()):
                    player.setWon(True)
                    print(player.getName() + " Won")
                    self.__ranking.append(player.getName())
                else:
                    print("Setting " + player.getName() + " position to " + str(player.getPosition()))
                    self.__players.append(player)

            if len(self.__players) < 2:
                print("Ranking ", self.__ranking)
                break

    def __getNewPosition(self, newPosition):
        for sn in self.__snakes:
            if (sn.getHead() == newPosition):
                print("Snake Bit")
                return sn.getTail()
        for la in self.__ladders:
            if (la.getStart() == newPosition):
                print("Climbed Ladder")
                return la.getEnd()
        return newPosition
