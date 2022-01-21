import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(function):
    def wrapper():
        start = time.time()
        function()
        end = time.time()
        final_time = end - start
        print('For {} the run time is: {}'.format(function.__name__, final_time))
    return wrapper

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(1000000000):
        i * i

fast_function()
slow_function()