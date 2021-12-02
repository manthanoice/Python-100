def formatting_name(first_name, last_name):
    if first_name == "" or last_name == "":
        return "You have givend empty string, please provide some value!"
    return first_name.title()+" "+last_name.title()

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Your name is: {}".format(formatting_name(first_name=first_name, last_name=last_name)))

#Typo