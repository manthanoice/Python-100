import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')
image = r'''Day-25\us-states-game-start\hhhhhh.gif'''
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv(r'Day-25\us-states-game-start\50_states.csv')

all_states = df['state'].to_list()
guessed_state = []

while(len(guessed_state)) < 50:
    answer_state = screen.textinput(title='{}/50 Correct names'.format(len(guessed_state)), prompt='Guess the name of another state: ').title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_state]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('Missing_state.csv')
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        toto = turtle.Turtle()
        toto.hideturtle()
        toto.penup()
        state_data = df[df.state == answer_state]
        toto.goto(int(state_data.x), int(state_data.y))
        toto.write(answer_state)