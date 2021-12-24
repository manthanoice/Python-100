try:
    file = open('example_file.txt')

except FileNotFoundError:
    file = open('example_file.txt', mode = 'w')
    file.write('YOOO WTF')

else:
    the_content = file.read()
    print(the_content)

finally:
    print('File was closed!')