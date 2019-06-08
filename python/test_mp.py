import threading
import multiprocessing
from multiprocessing import Process, Pool
import time

def foo(i):
    print('foo() print with {}'.format(i))
    time.sleep(0.1)


def MyProcess(Process):
    def __init__(self, arg):
        super(MyProcess, self).__init__()
        self.arg = arg
    
    def run(self):
        print('run() print with {}'.format(self.arg))
        time.sleep(0.1)


if __name__ == '__main__':
    '''
    for i in range(10):
        p = Process(target=foo, args=(i,))
        p.start()

    for i in range(10):
        p = MyProcess(i)
        p.start()
    '''

    with Pool(processes=4) as pool:
        # print(pool.map(foo, range(10)))

        for i in pool.imap_unordered(foo, range(10)):
            print(i)