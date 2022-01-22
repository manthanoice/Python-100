def logging_decorator(function):
    def wrapper(*args, **kwargs):
        print('You called {} function {}'.format(function.__name__, args))
        result = function(args[0], args[1], args[2], args[3])
        print('It returned {}'.format(result))
    return wrapper

@logging_decorator
def multiplication(a, b, c, d):
    return a*b*c*d

@logging_decorator
def addition(a, b, c, d):
    return a+b+c+d

multiplication(32,2,2,2)
addition(23,324, 32, 23)