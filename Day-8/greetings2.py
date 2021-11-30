def greet_with(name, city):
    print("Hey there {}".format(name))
    print("Oh nice, so {} you're from {}!".format(name, city))

the_name = input("What's your name? ")
the_city = input("Where are you from? ")
greet_with(the_name, the_city)