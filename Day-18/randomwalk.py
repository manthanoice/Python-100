import turtle as turtle
import random

angles = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

turtle.colormode(255)
tim = turtle.Turtle()

for i in range(300):
    tim.speed(20)
    tim.pensize(15)
    tim.forward(30)
    i = random.choice(angles)
    tim.right(i)
    tim.color(random_color())

screen = turtle.Screen()
screen.exitonclick()