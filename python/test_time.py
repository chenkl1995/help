import time

print( time.time() )
print( time.localtime(time.time()) )
print( time.asctime( time.localtime(time.time()) ) )
print( time.ctime() )

print(time.strftime('%Y-%m-%d_%H:%M:%S',time.localtime(time.time())))

# import datetime
# print(datetime.datetime())



import time
import functools
def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time()
        print('[{}] {}s'.format(func.__name__, end_time - start_time))
        return ret
    return wrapper

@timeit
def foo():
    for i in range(10):
        time.sleep(0.1)

foo()