import turtle as turtle

tim = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    tim.forward(100)

screen.listen()
screen.onkey(key='space', fun=move_forward)

screen.exitonclick()