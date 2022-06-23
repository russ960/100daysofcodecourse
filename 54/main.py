import time
current_time = time.time()
print(current_time)

def speed_calc_decorator(time_function):
    def timer_wrapper():
        t1 = time.time()
        time_function()
        t2 = time.time()
        print(f"{time_function.__name__} run speed: {t2 - t1}")
    return timer_wrapper

@speed_calc_decorator 
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator 
def slow_function():
    for i in range(100000000):
        i * i

fast_function()
slow_function()