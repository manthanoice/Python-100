print("LMAO would you like to find your and your crush's true love compatibility haha! 😶‍🌫️")
your_name = input("Enter your name: ").lower()
crush_name = input("Enter your crush's name: ").lower()
final_name = your_name + crush_name

true = 0
true += final_name.count('t')
true += final_name.count('r')
true += final_name.count('u')
true += final_name.count('e')
true = str(true)

love = 0
love += final_name.count('l')
love += final_name.count('o')
love += final_name.count('v')
love += final_name.count('e')
love = str(love)
answer = true+love

temp = int(answer)

if temp<10 or temp>90:
    print("Your score is {}. And you & {} is likely to have coke and mentos at movie theater".format(answer, crush_name))
elif temp>=11 and temp<=89:
    print("Your score is {}. And you & {} are alright together".format(answer, crush_name))
else:
    print("Your score is {} and F for you lmao".format(answer)) 