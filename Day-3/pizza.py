print("Dominos and pizza hut sucks, mummy makes better pizza at home!")
small = 15
medium = 20
large = 25
pep_s = 2
pep_regular = 3
extra_cheese = 1
size = input("What size of pizza do you want? S, M or L: ")
pepperoni = input("Do you want to add pepperoni to your {} pizza Y or N: ".format(size))
cheese = input("Do you want to add extra cheese to your {} pizza Y or N: ".format(size))
bill = 0
if pepperoni == 'Y' and cheese == 'Y':
    if size == 'S':
        bill += small+pep_s+extra_cheese
    elif size == 'M':
        bill += medium+pep_regular+extra_cheese
    else:
        bill += large+pep_regular+extra_cheese
elif pepperoni =='Y' and cheese == 'N':
    if size == 'S':
        bill += small+pep_s
    elif size == 'M':
        bill += medium+pep_regular
    else:
        bill += large+pep_regular
elif pepperoni =='N' and cheese =='Y':
    if size == 'S':
        bill += small+extra_cheese
    elif size == 'M':
        bill += medium+extra_cheese
    else:
        bill += large+extra_cheese
else:
    if size == 'S':
        bill += small
    elif size == 'M':
        bill += medium
    else:
        bill += large
print("Your total bill is: {}$".format(bill))