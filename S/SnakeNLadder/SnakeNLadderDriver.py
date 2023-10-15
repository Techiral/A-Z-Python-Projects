from Game import Game
from Player import Player


class SnakeNLadderDriver:

    def main(self):
        print("Enter Board size")
        n = int(input())
        print("Enter the number of players")
        np = int(input())
        print("Enter the number of Snakes")
        ns = int(input())
        print("Enter the number of Ladders")
        nl = int(input())

        game = Game(nl,ns,n)
        for i in range(np):
            print("Enter player name")
            pname = input()
            p = Player(pname)
            game.addPlayer(p)
        game.playGame()

sd = SnakeNLadderDriver()
sd.main()
