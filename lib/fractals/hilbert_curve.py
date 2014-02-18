import turtle
import math

def hilbert(n):
    t = turtle.Turtle()
    s = turtle.Screen()

    default_width = 500

    directions = ['up', 'right', 'down', 'left']

    # scaling
    x = y = - default_width / 2
    d = default_width // (2 ** n)

    t.up(); t.goto(x, y); t.down()

    def curve(direction):
        i = directions.index(direction)
        for direction in directions[i:] + directions[:i]: line(direction)

    def line(direction):
        if direction == 'up':
            t.goto(t.xcor(), t.ycor() + d)
        elif direction == 'right':
            t.goto(t.xcor() + d, t.ycor())
        elif direction == 'down':
            t.goto(t.xcor(), t.ycor() - d)
        elif direction == 'left':
            t.goto(t.xcor() - d, t.ycor())



    def hilbert_rec(n, direction):
        if n == 1:
            return curve(direction)
        else:
            if direction == 'up':
                hilbert_rec(n - 1, 'right')
                line('up')
                hilbert_rec(n - 1, 'up')
                line('right')
                hilbert_rec(n - 1, 'up')
                line('down')
                hilbert_rec(n - 1, 'left')
            elif direction == 'down':
                hilbert_rec(n - 1, 'left')
                line('down')
                hilbert_rec(n - 1, 'down')
                line('left')
                hilbert_rec(n - 1, 'down')
                line('up')
                hilbert_rec(n - 1, 'right')
            elif direction == 'left':
                hilbert_rec(n - 1, 'down')
                line('left')
                hilbert_rec(n - 1, 'left')
                line('down')
                hilbert_rec(n - 1, 'left')
                line('right')
                hilbert_rec(n - 1, 'up')
            elif direction == 'right':
                hilbert_rec(n - 1, 'up')
                line('right')
                hilbert_rec(n - 1, 'right')
                line('up')
                hilbert_rec(n - 1, 'right')
                line('left')
                hilbert_rec(n - 1, 'down')


    hilbert_rec(n, 'up')