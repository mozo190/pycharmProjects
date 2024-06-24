import time

current_time = time.time()
print(current_time)

def speed_calc_decoration(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"Time taken: {end - start}s")
        return wrapper()

