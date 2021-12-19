with open('E:\Python 100\Day-25\india state.txt') as file:
    the_states = file.readlines()

state_list = []
for state in the_states:
    stripped_state = state.strip()
    state_list.append(stripped_state)

the_list = []
for state in range(28):
    the_list.append(state_list[state])

print(the_list)