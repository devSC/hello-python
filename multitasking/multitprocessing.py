#coding=utf-8

'multiprocessing demo'

__author__ = 'Wilson'

'''
对于操作系统来说, 一个任务就是一个进程(process). 比如打开一个浏览器, 就启动一个浏览器进程.

在一个进程内部，要同时干多件事，就需要同时运行多个“子任务”，我们把进程内的这些“子任务”称为线程（Thread）。

对于进程来说, 一个进程中至少有一个线程.


对于Python,多任务的实现有3种方式：

多进程模式；
多线程模式；
多进程+多线程模式。
'''


'''
实现多进程(multiprocessing)

Unix/Linux操作系统提供了一个 fork() 系统调用, 调用一次后, 分别在当前进程和复制了一份的子进程内各自返回, 总共返回2次, 子进程永远返回 0 , 父进程 返回子进程的 ID, 子进程可以通过 getppid() 拿到父进程 ID .
'''

import os

def testFork():
    print('Process (%s) start...' % os.getpid())

    pid = os.fork()

    if pid == 0:
        print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
    else:
        print('I (%s) just created a child process (%s).' % (os.getpid(), pid))

    '''
    log:

    Process (18048) start...
    I (18048) just created a child process (18049).
    I am child process (18049) and my parent is 18048.
    '''

# testFork()




'''
multiprocessing模块是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象
'''

from multiprocessing import Process

#子进程执行的任务
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

def testProcessing():
    if __name__ == "__main__":
        print('Parent process %s.' % os.getpid())
        p = Process(target=run_proc, args=('test',))
        print('Child process will start')
        p.start()
        p.join()  # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
        print('Child process end.')

#testProcessing()
'''
#log:

Parent process 18197.
Child process will start
Run child process test (18198)...
Child process end.
'''



'''
Pool 进程池

如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''

from multiprocessing import Pool
import time, random

def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

def testPool():
    if __name__ == '__main__':
        p = Pool(4) #最多执行4个任务
        for i in range(5):
            p.apply_async(long_time_task, args=(i,))

        print('watting for all subprocesses done...')
        p.close() #调用close()之后就不能继续添加新的Process了。
        p.join() #join()方法会等待所有子进程执行完毕, 调用join()之前必须先调用close()
        print('All subprocesses done.')

#testPool()

'''
#log:

watting for all subprocesses done...
Run task 0 (18424)...
Run task 1 (18425)...
Run task 2 (18426)...
Run task 3 (18427)...
Task 2 runs 0.68 seconds.
Run task 4 (18426)... #等待前面执行完一个, 才开始执行
Task 0 runs 1.32 seconds.
Task 3 runs 1.75 seconds.
Task 1 runs 2.31 seconds.
Task 4 runs 2.31 seconds.
All subprocesses done.
'''


'''
子进程

很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出。

subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
'''

import subprocess


def testSubprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code: ', r)

#在Python代码中运行命令nslookup www.python.org，这和命令行直接运行的效果是一样的：
# testSubprocess()

'''
#log:

$ nslookup www.python.org
Server:		1.2.4.8
Address:	1.2.4.8#53

Non-authoritative answer:
www.python.org	canonical name = python.map.fastly.net.
Name:	python.map.fastly.net
Address: 151.101.72.223

Exit code:  0
'''


#如果子进程还需要输入，则可以通过communicate()方法输入：
def testSubprocess2():
    print('$ nslookup')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n') #输入
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)

testSubprocess2()

'''
上面的代码相当于在命令行执行命令nslookup，然后手动输入：

set q=mx
python.org
exit
'''

'''
#log:


$ nslookup
Server:		1.2.4.8
Address:	1.2.4.8#53

Non-authoritative answer:
python.org	mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
python.org	nameserver = ns3.p11.dynect.net.
python.org	nameserver = ns1.p11.dynect.net.
python.org	nameserver = ns2.p11.dynect.net.
python.org	nameserver = ns4.p11.dynect.net.
mail.python.org	internet address = 188.166.95.178
mail.python.org	has AAAA address 2a03:b0c0:2:d0::71:1


Exit code: 0
'''


'''
进程间通信

Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来给进程交换数据。
'''
from multiprocessing import Queue
# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

def testQueue():
    if __name__ == '__main__':
        # 父进程创建Queue，并传给各个子进程：
        q = Queue()
        pw = Process(target=write, args=(q,))
        pr = Process(target=read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 启动子进程pr，读取:
        pr.start()
        # 等待pw结束:
        pw.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:
        pr.terminate()


testQueue()

'''
#log:

Process to write: 18760
Put A to queue...
Process to read: 18761
Get A from queue.
Put B to queue...
Get B from queue.
Put C to queue...
Get C from queue.
'''


'''
总之:

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
'''