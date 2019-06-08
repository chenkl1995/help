import os

# http://github.lesschina.com/python/base/concurrency/1.%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B%EF%BD%9E%E8%BF%9B%E7%A8%8B%E5%85%88%E5%AF%BC%E7%AF%87.html
# https://github.com/lotapp/BaseCode/tree/master/python/5.concurrent/Linux
def test_fork():
    print("准备测试～PID: %d" % os.getpid())
    pid = os.fork()     # fork()一次调用，两次返回
    if pid == 0:        # 子进程永远返回0，而父进程返回子进程的ID
        print("子进程：PID: %d, PPID: %d" % (os.getpid(), os.getppid()))
    elif pid > 0:
        print("父进程：PID: %d, PPID: %d" % (os.getpid(), os.getppid()))
    print("PID: %d,我是卖报的小行家，大风大雨都不怕" % os.getpid())

# 各个进程地址空间中数据是完全独立的
def test_fork2():
    num = 100
    pid = os.fork()
    if pid == 0:    # 子进程
        num += 10
    elif pid > 0:
        num += 20
    print("PID: %d，PPID: %d，Num=%d" % (os.getpid(), os.getppid(), num))

def test_orphan_process():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        time.sleep(1)  # 睡1s
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
    print("pid=%d,over" % os.getpid())

def test_zombie_process():
    pid = os.fork()
    if pid == 0:
        print("子进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
    elif pid > 0:
        print("父进程：Pid=%d,PPID=%d" % (os.getpid(), os.getppid()))
        while True:
            print("父亲我忙着呢，没时间管你个小屁孩")
            time.sleep(1)
    print("pid=%d,over" % os.getpid())


if __name__ == '__main__':
    help(os.fork)
    test_fork()
    # > ps aux | grep [pid]
    test_fork2()
    # > ps ef
    # pid = 0, 1, 2, ...
    # > pstree -ps