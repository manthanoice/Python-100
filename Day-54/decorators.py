from numpy import inner


def add(n1, n2):
    return n1+n2

def multiply(n1, n2):
    return n1*n2

def subtract(n1, n2):
    return n1-n2

def divide(n1, n2):
    return n1/n2

def modulo(n1, n2):
    return n1%n2

#functions can be passed as arguments
def calculate(calc, n1, n2):
    return calc(n1, n2)

answer = calculate(modulo, 21, 22)
print(answer)

#nested functions

def outer():
    print('I am outer')
    def inner():
        print('I am inner')
    inner()

outer()

#functions can be returned from another functions
def outer():
    print('I am outer')
    def nested_function():
        print('I am inner')
    return nested_function

inner_function = outer()
inner_function()