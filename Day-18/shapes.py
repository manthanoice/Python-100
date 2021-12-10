import turtle as turtle
import random

colors = ['dark red', 'yellow', 'red', 'dark green', 'blue', 'dark gray', 'dim gray']

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

turtle.colormode(255)
tim = turtle.Turtle()

def draw_shape(num_slides):
    angle = 360//num_slides
    for i in range (num_slides):
        tim.forward(100)
        tim.right(angle=angle)

for i in range(3, 10):
    tim.speed(10)
    tim.color(random_color())
    draw_shape(i)

screen = turtle.Screen()
screen.exitonclick()