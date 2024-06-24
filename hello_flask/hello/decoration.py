import time

current_time = time.time()


# print(current_time)

def speed_calc_decoration(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"{func.__name__} Time taken: {end - start}s")

    return wrapper()


@speed_calc_decoration
def fast_function():
    print("I'm a fast function")


@speed_calc_decoration
def slow_function():
    time.sleep(2)
    print("I'm a slow function")
