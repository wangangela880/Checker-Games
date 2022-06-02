'''
Yu Wang
CS 5001, Fall 2021
Milestone 4

Checker Game
'''

import turtle


class titles(turtle.RawTurtle):
    def __init__(self, screen):
        self.screen = screen
        self.createPen()

    def createPen(self):
        '''
        Function -- createPen
            creates the turtle
        Parameter:
            self
        '''
        super(titles, self).__init__(self.screen)
        self.hideturtle()
        self.speed(0)
        self.width(3)
        self.up()
