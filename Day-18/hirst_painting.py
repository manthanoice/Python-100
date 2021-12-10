import turtle as turtle
import random

final_list = [(229, 249, 73), (229, 237, 253), (67, 252, 194), (17, 184, 82), (19, 15, 96), (218, 153, 94), (74, 37, 23), (94, 1, 56), (59, 4, 180), (247, 102, 203), (28, 245, 41), (248, 21, 135), (168, 3, 123), (6, 99, 40), (100, 179, 5), (50, 15, 253), (106, 172, 243), (172, 92, 13), (11, 92, 180), (64, 114, 247), (183, 183, 250), (183, 2, 1), (249, 21, 18), (53, 98, 1), (76, 248, 252), (4, 181, 187), (19, 151, 58), (172, 47, 128), (2, 98, 101), (237, 161, 212), (191, 11, 145), (4, 74, 28), (252, 11, 7), (244, 162, 157), (202, 253, 0), (15, 251, 198)]

turtle.colormode(255)
tim = turtle.Turtle()
tim.hideturtle()

def hirst(space, square_size):
    for i in range(square_size):
        for j in range(square_size):
            tim.dot(20, random.choice(final_list))
            tim.forward(space)
        tim.backward(space*square_size)
        tim.right(90)
        tim.forward(space)
        tim.left(90)
tim.speed(20)
tim.penup()
hirst(50, 10)
screen = turtle.Screen()
screen.exitonclick()