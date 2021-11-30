def greet(name):
    print("Hey {}! Good morning!".format(name))
    print("How's your day going, {}?".format(name))
    print("What's your favorite series? Please don't say FRIENDS yar {}! xD".format(name))

the_name = input("Enter who you wanna greet: ")
greet(the_name)