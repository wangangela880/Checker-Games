'''
Final project - milestone 1
CS 5001, Fall 2021
Yu Wang
Started with the final project, milestone 1.
'''
import turtle


NUM_SQUARES = 8
SQUARE = 50
SQUARE_COLORS = ("light gray", "white", "red", "black")


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.begin_fill()
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def draw_circle(a_turtle, size):
    '''
        Function -- draw_circle
            Draw a circle of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the circle
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    a_turtle.begin_fill()
    a_turtle.pendown()
    a_turtle.circle(size)
    a_turtle.end_fill()
    a_turtle.penup()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    print("Clicked at ", x, y)


def main():
    board_size = NUM_SQUARES * SQUARE
    window_size = board_size + SQUARE
    turtle.setup(window_size, window_size)

    # Set the drawing canvas size. The should be actual board size
    turtle.screensize(board_size, board_size)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.color("black", "white")

    # YOUR CODE HERE
    # Step 1 - the board outline
    corner = -board_size / 2
    pen.setposition(corner, corner)
    draw_square(pen, board_size)

    # Step 2 & 3 - the checkerboard squares
    pen.color("black", SQUARE_COLORS[0])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.setposition(corner + SQUARE * col, corner + SQUARE * row)
                draw_square(pen, SQUARE)
                print(corner + SQUARE * col, corner + SQUARE * row)

    pen.color("black", SQUARE_COLORS[2])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if (row != 3 and row != 4 and row != 2 and row != 1 and row != 0
               and col % 2 != row % 2):
                pen.setposition(corner + SQUARE * col + 25, corner +
                                SQUARE * row)
                draw_circle(pen, 25)

    pen.color("black", SQUARE_COLORS[3])
    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if (row != 5 and row != 6 and row != 7 and row != 4 and row != 3
               and col % 2 != row % 2):
                pen.setposition(corner + SQUARE * col + 25, corner
                                + SQUARE * row)
                draw_circle(pen, 25)

    # Click handling
    screen = turtle.Screen()
    screen.onclick(click_handler)
    turtle.done()


if __name__ == "__main__":
    main()
