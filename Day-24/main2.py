#Firstly, opening and reading the file

with open('.\Day-24\my_file.txt') as file:
    contents = file.read()
    print(contents)

#Secondly, writing in the file

with open('.\Day-24\my_file.txt', mode='a') as file:
    the_add = file.write('\nHehe')

#Creating new file from scratch, if you try to open a file that has different name, python will create that file for you! xD

with open('new_file.txt', mode='w') as file:
    file.write('Ooohhhh la la')