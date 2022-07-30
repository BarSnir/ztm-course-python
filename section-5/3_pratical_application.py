from time import time

def performance(fn):
    def warp_func(*args, **kwargs):
        t1 = time()
        results = fn(*args, **kwargs)
        t2 = time()
        print(f'The function took {t2-t1} seconds.')
        return results
    return warp_func

@performance
def long_time():
    for i in range(100000000):
        i * 5

@performance
def short_time():
    for i in range(10000):
        i * 5

long_time()
short_time()