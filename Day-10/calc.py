logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)

def addition(a, b):
    return a+b

def subtraction(a, b):
    return a-b

def multiplication(a, b):
    return a*b

def division(a, b):
    return a/b

operations = {
    '+': addition,
    '-': subtraction,
    '*': multiplication,
    '/': division
}

def calc():
    n1 = float(input("Enter the first number: "))
    should_continue = True
    while should_continue:
        n2 = float(input("Enter next number: "))
        for operation in operations:
            print(operation)
        selected_operation = input("Select operation from above list: ")
        the_operation = operations[selected_operation] #This is basically which method you're calling from addition, subtraction, multi, divison!
        answer = the_operation(n1, n2)
        print("{} {} {} = {}".format(n1, selected_operation, n2, answer))
        more_continue = input("Do you want to continue? 'y' or 'n': ")
        if more_continue == 'y':
            n1 = answer
        elif more_continue == 'n':
            should_continue = False
            calc()
        else:
            print("Either type 'y' or 'n'")
            should_continue = False
calc()

#Just typo Day-10