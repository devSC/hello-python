#coding=utf-8

#multithread demo

__author__ = 'Wilson'


'''
多任务可以由多进程完成，也可以由一个进程内的多线程完成。

一个进程至少有一个线程。

Python的线程是真正的Posix Thread，而不是模拟出来的线程。


_thread和threading，

_thread是低级模块，

threading是高级模块，对_thread进行了封装。

绝大多数情况下，我们只需要使用threading这个高级模块。
'''

import time, threading
#启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：

def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

def testThread():
    print('thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()

    print('thread %s ended.' % threading.current_thread().name)

    '''
    #log: 
    thread MainThread is running...
    thread LoopThread is running...
    thread LoopThread >>> 1
    thread LoopThread >>> 2
    thread LoopThread >>> 3
    thread LoopThread >>> 4
    thread LoopThread >>> 5
    thread LoopThread ended.
    thread MainThread ended.
    '''

# testThread()


'''
Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。

来看看多个线程同时操作一个变量怎么把内容给改乱了：
'''

balance = 0
lock = threading.Lock()

def change_it(n):
    #先存后取, 结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

        #用try...finally来确保锁一定会被释放



def testBalance():
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print(balance)

testBalance()


# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()


def test_thread_local():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()

test_thread_local()

'''
ThreadLocal可以为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，

这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

一个ThreadLocal变量虽然是全局变量，但每个线程都只能读写自己线程的独立副本，互不干扰。ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''