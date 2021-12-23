try:
    file = open('example_file.txt')
except FileNotFoundError:
    file = open('example_file.txt', mode = 'w')
    file.write('YOOO WTF')