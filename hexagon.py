#Write a Python program to draw a hexagon and fill it with red color.

import turtle

t = turtle.Turtle()
t.color("red")
t.begin_fill()

for _ in range(6):
    t.forward(100)
    t.right(60)

t.end_fill()
turtle.done()