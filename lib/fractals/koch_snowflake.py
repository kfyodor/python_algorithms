import turtle
import math
    
def snowflake(n):
    t, s = turtle.Turtle(), turtle.Screen()

    default_length = 400
    x = y = -default_length / 2

    t.speed(0)
    t.up()
    t.goto(x, -y - 100)
    t.down()

    def draw_line(length): 
        t.forward(length)

    def draw(n, length):
        if n == 1:
            draw_line(length)
        else:
            snowflake_rec(n - 1, length)

    def snowflake_rec(n, length):
        if n == 0:
            draw_line(length)
        else:
            draw(n, length / 3)
            t.left(60)
            draw(n, length / 3)
            t.right(120)
            draw(n, length / 3)
            t.left(60)
            draw(n, length / 3)

    snowflake_rec(n, default_length)
    t.right(120)
    snowflake_rec(n, default_length)
    t.right(120)
    snowflake_rec(n, default_length)