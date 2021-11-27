marks = input("Enter marks: ").split()
for i in range(0, len(marks)):
    marks[i] = int(marks[i])
highest = 0
for i in marks:
    if i > highest:
        highest = i
print("Highest number is {}".format(highest))