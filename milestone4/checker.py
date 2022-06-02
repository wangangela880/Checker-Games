
'''
Yu Wang
CS 5001, Fall 2021
Milestone 4

Checker Game
'''

from boards import board
import random


def onboard(x, y):
    '''
        Function -- onboard
            checks if (x, y) are on the board
        Parameter:
            x -- the value of x axis
            y -- the value of y axis
        Returns:
            if (x, y) are on the board
    '''
    if((x in range(8)) and (y in range(8))):
        return True
    else:
        return False


class checkers:
    def __init__(self, screen):
        self.screen = screen
        self.resetGame()

    def resetGame(self):
        '''
        Function -- resetGame
            resets the grid that stores game data
        Parameter:
            self
        '''
        self.turn = 1
        self.createboard()

    def createboard(self):
        '''
        Function -- createboard
            create the grid that stores the game data
        Parameter:
            self
        '''
        self.grid = [
            [None]*8, [None]*8, [None]*8, [None]*8,
            [None]*8, [None] * 8, [None]*8, [None]*8
            ]

        for x in range(8):
            for y in range(8):
                self.grid[x][y] = board(self.screen)
                self.grid[x][y].moveboard(x, y)
                if(((x + y) % 2) == 1):
                    self.grid[x][y].colored = True
                    if(y in [0, 1, 2]):
                        self.grid[x][y].piece = True
                        self.grid[x][y].player = 1

                    if(y in [5, 6, 7]):
                        self.grid[x][y].piece = True
                        self.grid[x][y].player = 2
                self.grid[x][y].draw()
        self.highlightedSpaces = []
        self.spacechoosed = False

    def mouseEvent(self, draw_x, draw_y):
        '''
        Function -- mouseEvent
            funcion is called whenever the window is clicked
        Parameter:
            self
            draw_x
            draw_y
        '''
        x = int((draw_x + 4*board.boardSize) // board.boardSize)
        y = int((draw_y + 4*board.boardSize) // board.boardSize)
        is_move = False

        if(onboard(x, y)):
            if((self.grid[x][y].piece)
               and (self.grid[x][y].player == self.turn)):
                if self.grid[x][y].player == 1:
                    print("It is your turn! You are at (" + str(x)
                          + ',' + str(y) + ")")
                if(self.spacechoosed != 0):
                    self.deselectAll()
                moves = self.findMoves(x, y)
                jumps = self.findJumps(x, y)
                for move in moves:
                    self.grid[move[0]][move[1]].choosed = 1
                    self.highlightedSpaces.append((move[0], move[1]))
                    self.grid[move[0]][move[1]].draw()
                if not moves:
                    for jump in jumps:
                        self.grid[jump[0]][jump[1]].choosed = 2
                        self.highlightedSpaces.append((jump[0], jump[1]))
                        self.grid[jump[0]][jump[1]].draw()
                self.spacechoosed = (x, y)

            elif(self.grid[x][y].choosed == 1):
                self.movepiece(self.spacechoosed, (x, y))
                self.deselectAll()
                is_move = True
                # self.endTurn()

            elif(self.grid[x][y].choosed == 2):
                self.jumppiece(self.spacechoosed, (x, y))
                jumps = self.findJumps(x, y)
                is_move = True
                if(jumps != []):
                    self.deselectAll()
                    self.spacechoosed = (x, y)
                    for move in jumps:
                        self.grid[move[0]][move[1]].choosed = 2
                        self.highlightedSpaces.append((move[0], move[1]))
                        self.grid[move[0]][move[1]].draw()
                else:
                    self.deselectAll()
                    # self.endTurn()
            else:
                self.deselectAll()

            if not is_move:
                return

            list = []
            for start_x in range(8):
                for start_y in range(8):
                    if self.grid[start_x][start_y].player == 2:
                        moves_2 = self.findMoves(start_x, start_y)
                        jumps_2 = self.findJumps(start_x, start_y)
                        for move in moves_2:
                            list.append({
                                 'start_x': start_x,
                                 'start_y': start_y,
                                 'x': move[0],
                                 'y': move[1],
                                 'op': 1
                             })
                        for jump in jumps_2:
                            list.append({
                                 'start_x': start_x,
                                 'start_y': start_y,
                                 'x': jump[0],
                                 'y': jump[1],
                                 'op': 2
                             })

            target = list[random.randint(0, len(list)-1)]
            if(target['op'] == 1):
                self.movepiece((target['start_x'], target['start_y']),
                               (target['x'], target['y']))
                self.deselectAll()
                # self.endTurn()

            else:
                self.jumppiece((target['start_x'], target['start_y']),
                               (target['x'], target['y']))
                jumps = self.findJumps(target['x'], target['y'])
                if(jumps != []):
                    self.deselectAll()
                    self.spacechoosed = (target['x'], target['y'])
                    for move in jumps:
                        self.grid[move[0]][move[1]].choosed = 2
                        self.highlightedSpaces.append((move[0], move[1]))
                        self.grid[move[0]][move[1]].draw()
                else:
                    self.deselectAll()
                    # self.endTurn()

            if not self.is_lose(1):
                print('Computer Win!')
                return
            elif not self.is_lose(2):
                print('Player Win!')
                return

    def deselectAll(self):
        '''
        Function -- deselectAll
            deselects all of the choosed board spaces
        Parameter:
            self
        '''
        for space in self.highlightedSpaces:
            self.grid[space[0]][space[1]].choosed = 0
            self.grid[space[0]][space[1]].draw()
        self.spacechoosed = False

    def findMoves(self, x, y):
        '''
        Function -- findMoves
        Parameter:
            self
            x -- the value of x axis
            y -- the value of y axis
        Return:
            returns moves available to a piece at (x, y)
        '''
        if(self.grid[x][y].player == 1):
            moves = [(-1, 1), (1, 1)]
            if(self.grid[x][y].king == 1):
                moves += [(-1, -1), (1, -1)]

        elif(self.grid[x][y].player == 2):
            moves = [(-1, -1), (1, -1)]
            if(self.grid[x][y].king == 1):
                moves += [(-1, 1), (1, 1)]

        coords = []
        for move in moves:
            x1 = x + move[0]
            y1 = y + move[1]
            if((onboard(x1, y1)) and (not self.grid[x1][y1].piece)):
                coords.append((x1, y1))
        return coords

    def findJumps(self, x, y):
        '''
        Function -- findJumps
        Parameter:
            self
            x -- the value of x axis
            y -- the value of y axis
        Return:
            returns coords of jumps available to a piece at coords (x, y)
        '''
        if(self.grid[x][y].player == 1):
            moves = [(-1, 1), (1, 1)]
            if(self.grid[x][y].king == 1):
                moves += [(-1, -1), (1, -1)]

        elif(self.grid[x][y].player == 2):
            moves = [(-1, -1), (1, -1)]
            if(self.grid[x][y].king == 1):
                moves += [(-1, 1), (1, 1)]

        coords = []
        for move in moves:
            x1 = x + move[0]
            y1 = y + move[1]
            x2 = x + 2*move[0]
            y2 = y + 2*move[1]
            if((onboard(x2, y2)) and (not self.grid[x2][y2].piece)):
                if((self.grid[x1][y1].piece)):
                    if((self.grid[x][y].player == 1)
                       and (self.grid[x1][y1].player == 2)):
                        coords.append((x2, y2))
                    elif((self.grid[x][y].player == 2)
                         and (self.grid[x1][y1].player == 1)):
                        coords.append((x2, y2))
        return coords

    def movepiece(self, boardA, boardB):
        '''
        Function -- movepiece
            moves a piece from boardA to boardB
        Parameter:
            self
            boardA -- the original place
            boardB -- the target place
        '''
        self.grid[boardB[0]][boardB[1]].importpiece(
            self.grid[boardA[0]][boardA[1]])
        self.grid[boardA[0]][boardA[1]].clearpiece()
        self.kingpiece(boardB[0], boardB[1])

    def jumppiece(self, boardA, boardC):
        '''
        Function -- jumppiece
            moves piece from boardA to boardC by jumping over
        Parameter:
            self
            boardA -- the original place
            boardC -- the target place
        '''
        boardB = (int((boardC[0]+boardA[0])/2), int((boardC[1]+boardA[1])/2))
        self.grid[boardC[0]][boardC[1]].importpiece(
            self.grid[boardA[0]][boardA[1]])
        self.grid[boardB[0]][boardB[1]].clearpiece()
        self.grid[boardA[0]][boardA[1]].clearpiece()
        self.kingpiece(boardC[0], boardC[1])

    def kingpiece(self, x, y):
        '''
        Function -- kingpiece
            kings the piece at coords (x, y) if it has reached it's kings row
        Parameter:
            self
            x -- the value of x axis
            y -- the value of y axis
        '''
        if((self.grid[x][y].player == 1) and (y == 7)):
            self.grid[x][y].king = True
            self.grid[x][y].draw()
        elif((self.grid[x][y].player == 2) and (y == 0)):
            self.grid[x][y].king = True
            self.grid[x][y].draw()

    def endTurn(self):
        '''
        Function -- endTurn
            ends the current turn
        Parameter:
            self
        '''
        if(self.turn == 1):
            self.turn = 2
        elif(self.turn == 2):
            self.turn = 1

    def is_lose(self, player):
        list = []
        for x in range(8):
            for y in range(8):
                if self.grid[x][y].player == player:
                    moves = self.findMoves(x, y)
                    jumps = self.findJumps(x, y)
                    for move in moves:
                        list.append((move[0], move[1]))
                    if not moves:
                        for jump in jumps:
                            list.append((jump[0], jump[1]))
        return list
