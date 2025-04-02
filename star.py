#How to draw a star shape using the Turtle module?

import turtle

t = turtle.Turtle()
t.color("blue")

for _ in range(5):
    t.forward(100)
    t.right(144)

turtle.done()