import math
def calc(height, width, coverage):
    return ((height*width)/coverage)

height = int(input("Enter height of the wall: "))
width = int(input("Enter width of the wall: "))
coverage = int(input("Enter coverage by cans: "))

print("You will need {} cans!".format(math.ceil(calc(height=height, width=width, coverage=coverage))))