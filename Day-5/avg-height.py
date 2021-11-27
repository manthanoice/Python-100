heights = input("Enter heights: ").split()
for i in range(0, len(heights)):
    heights[i] = int(heights[i])
answer = 0
for i in heights:
    answer+=i
the_answer = round((answer)/len(heights))
print("The average height is {} CMs!".format(the_answer))