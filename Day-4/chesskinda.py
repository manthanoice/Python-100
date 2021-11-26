row1 = ['🟥', '🟥', '🟥']
row2 = ['🟥', '🟥', '🟥']
row3 = ['🟥', '🟥', '🟥']
map = [row1, row2, row3]
print("{}\n{}\n{}".format(row1, row2, row3))
num = input("Enter where you want to put the number: ")
num1 = int(num[0])
num2 = int(num[1])
map[num1 - 1][num2 - 1] = 'X'
print("{}\n{}\n{}".format(row1, row2, row3))

#Is it just me or you can do this thing easily using numpy :P