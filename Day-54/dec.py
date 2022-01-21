import time

def delay_function(function):
    def wrapper_function():
        time.sleep(2)
        #Do somethingn before
        function()
        #Do something afterwards
        time.sleep(2)
        function()
    return wrapper_function

@delay_function
def say_hello():
    print('Hello bitches')

@delay_function
def say_bye():
    print('Bye bitches')

say_hello()
say_bye()