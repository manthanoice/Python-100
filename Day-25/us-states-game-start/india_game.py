from turtle import *
import turtle

toto = Turtle()
screen = Screen()
image = '''E:\Python 100\Day-25\India map.gif'''
screen.addshape(image)
toto.shape(image)

with open('E:\Python 100\Day-25\india state.txt') as file:
    the_states = file.readlines()

state_list = []
for state in the_states:
    stripped_state = state.strip()
    state_list.append(stripped_state)

for i in range(28):
    def get_mouse_click(x, y, state):
        the_list = []
        for state in range(28):
            the_list.append((x, y, state_list[state]))
            print(the_list)

turtle.onscreenclick(get_mouse_click)
turtle.mainloop()
screen.exitonclick()