'''
Yu Wang
CS 5001, Fall 2021
Milestone 4

Checker Game
'''

import turtle
from checker import checkers


def main():
    sc = turtle.Screen()
    sc.tracer(0, 0)
    game = checkers(sc)
    sc.onclick(game.mouseEvent)
    sc.mainloop()


if __name__ == "__main__":
    main()
