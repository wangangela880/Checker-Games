'''
Yu Wang
CS 5001, Fall 2021
Milestone 4

Checker Game
'''


import turtle


class board(turtle.RawTurtle):
    boardSize = 60
    size_of_board = 20
    size_of_king = 10

    def __init__(self, screen):
        self.screen = screen
        self.game_status()
        self.newPen()

    def newPen(self):
        '''
        Function -- newPen
            ready for draw
        Parameter:
            self
        '''
        super(board, self).__init__(self.screen)
        self.hideturtle()
        self.speed(0)
        self.width(2)
        self.up()

    def game_status(self):
        '''
        Function -- game_status
            sets the board's attributes
        Parameter:
            self
        '''
        self.boardX = 0
        self.boardY = 0
        self.colored = False
        self.choosed = 0
        self.piece = False
        self.player = 0
        self.king = False

    def clearpiece(self):
        '''
        Function -- clearpiece
            removes the piece from the board
        Parameter:
            self
        '''
        self.choosed = False
        self.piece = False
        self.player = 0
        self.king = False
        self.draw()

    def importpiece(self, boardObj):
        '''
        Function -- importpiece
            imports all attributes from another board object
        Parameter:
            self
            boardObj -- the instance with clase board
        '''
        self.colored = boardObj.colored
        self.piece = boardObj.piece
        self.player = boardObj.player
        self.king = boardObj.king
        self.draw()

    def moveboard(self, newX, newY):
        '''
        Function -- moveboard
            places the board at a new set of coords
        Parameter:
            self
            gX -- new x
            gY -- new y
        '''
        self.boardX = newX
        self.boardY = newY

    def draw(self):
        '''
        Function -- draw
            draws the board and the pieces
        Parameter:
            self
        '''
        draw_x = int(self.boardX*board.boardSize - 4*board.boardSize)
        draw_y = int(self.boardY*board.boardSize - 4*board.boardSize)
        self.clear()

        self.goto(draw_x, draw_y)
        self.seth(0)
        self.down()
        if(self.colored):
            if(self.choosed in [1, 2]):
                self.color((0, 0, 0), (0.5, 1, 0.5))
            else:
                self.color((0, 0, 0), (0.75, 0.75, 0.75))
            self.begin_fill()
        for f in range(4):
            self.fd(board.boardSize)
            self.left(90)
        self.end_fill()
        self.up()

        if(self.piece):
            self.goto(draw_x + 0.5*board.boardSize,
                      draw_y + 0.5*board.boardSize - board.size_of_board)
            if(self.player == 1):
                self.color((0, 0, 0), (0, 0, 0))
            elif(self.player == 2):
                self.color((1, 0.5, 0.5), (1, 0.5, 0.5))
            else:
                self.color((0, 0, 0), (1, 0.5, 1))
            self.down()
            self.begin_fill()
            self.circle(board.size_of_board, 360, 16)
            self.end_fill()
            self.up()

            if(self.king):
                self.goto(draw_x + 0.5*board.boardSize, draw_y +
                          0.5*board.boardSize - board.size_of_king)
                self.color((0, 0, 0), (1, 0.85, 0))
                self.down()
                self.begin_fill()
                self.circle(board.size_of_king, 360, 16)
                self.end_fill()
                self.up()
