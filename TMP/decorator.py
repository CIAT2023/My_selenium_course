
import time
def timeit(func):
    def wrapper():
        start = time.time()
        result = func()
        print(time.time() - start)
        return result
    return wrapper

@timeit
def gen():
    l = [x for x in range(10**4) if x % 2 ==0]
    return l

gen()