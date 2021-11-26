import random

names = input("Enter names of people seperated by a comma: ")
names_final = names.split(", ")
n = len(names_final)
answer = names_final[random.randint(0, n-1)]
print("{} Will pay the bill!".format(answer))