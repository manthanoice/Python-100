number = int(input("Which number do you want to check: "))

if number % 2 == 0:
    print("{} is an even number.".format(number))
else:
    print("{} is an odd number.".format(number))