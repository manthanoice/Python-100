import turtle as turtle
import random

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

turtle.colormode(255)
tim = turtle.Turtle()

for i in range(120):
    tim.speed(20)
    tim.color(random_color())
    tim.circle(300)
    tim.left(3)

screen = turtle.Screen()
screen.exitonclick()