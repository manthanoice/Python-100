from turtle import *

lalu = Turtle()
lalu.shape('turtle')
lalu.color("sienna")
for i in range(0, 4):
    lalu.forward(100)
    lalu.right(90)
    lalu.forward(100)
    lalu.right(90)
    lalu.forward(100)
    lalu.right(90)
    lalu.forward(100)

screen = Screen()
screen.exitonclick()