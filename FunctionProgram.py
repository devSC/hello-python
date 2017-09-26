#coding=utf-8


'''
函数式编程


函数就是面向过程的程序设计的基本单元。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！


Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。
'''


'''
高阶函数

高阶函数英文叫Higher-order function

高阶函数特征:
- 变量可以指向函数
- 函数名也是变量
- 传入函数

'''

f = abs
print(f, abs)
#log: <built-in function abs> <built-in function abs>

#结论：函数本身也可以赋值给变量，即：变量可以指向函数。




'''
函数名也是变量

那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！

如果把abs指向其他对象，会有什么情况发生？
'''
#abs = 10
#abs(10)
#log: TypeError: 'int' object is not callable
#把abs指向10后，就无法通过abs(-10)调用该函数了！因为abs这个变量已经不指向求绝对值函数而是指向一个整数10！



'''
传入函数

既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
'''

def add(x, y, f):
    return f(x) + f(y)

print(add(-5, 6, abs))
#log: 11

#编写高阶函数，就是让函数的参数能够接收别的函数。
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。



'''
MAP

map()作为高阶函数，事实上它把运算规则抽象了
'''

def f(x):
    return x * x

L = [1, 2, 3];
r = map(f, L)
print(list(r))
#log: [1, 4, 9]
print(list(map(str, L)))


'''
reduce

reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
'''
from functools import reduce

def fn(x, y):
    print(x, y)
    return x * 10 + y

print(reduce(fn, L))
#log: 123

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('1234567'))

# 配合闭包还可以简化
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y : x * 10 + y, map(char2num, s))

print(str2int('0981234567'))



'''
函数作为返回值
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
print(lazy_sum(1, 3, 4, 6, 7)())
#log: 21


'''
闭包

注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
'''
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#这里因为引用变量i的原因, f1, f2, f3的值都为 9.

'''
返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。



可以通过再创建一个函数，来解决循环变量引用的问题. 
用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
'''

def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
#log:
#1
#4
#9


'''
匿名函数

此处 lambda 声明的为匿名函数
'''

list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

#匿名函数lambda x: x * x实际上就是：

def f(x):
    return x * x

'''
关键字lambda表示匿名函数，冒号前面的x表示函数参数。

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
'''


'''
装饰器

假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
'''

def now():
    print('2017-09-25')


#本质上，decorator就是一个返回函数的高阶函数。
def log(func):

    #wrapper()函数的参数定义是(*args, **kw)，
    #因此，wrapper()函数可以接受任意参数的调用。
    #在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

@log
def now():
    print('2017-09-25')

print(now())

#log:
#call now():
#2017-09-25

#把@log放到now()函数的定义处，相当于执行了语句：
now = log(now)


#带参数的log函数 本质就是利用高阶函数.
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('excute')
def now():
    print('2017-09-25')

print(now())
#log:
#excute now():
#2017-09-25


#@log(text)相当于
now = log('execute')(now)


#但目前now 的name遍了
print(now.__name__)
#log: wrapper


#Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools

def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

#或者针对带参数的:
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator



def int2(x, base=2):
    return int(x, base)

'''
偏函数

functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义int2()，可以直接使用下面的代码创建一个新的函数int2：
'''

int2 = functools.partial(int, base=2)
print(int2('10000000'))
#log: 128

max2 = functools.partial(max, 10)
#实际上会把10作为*args的一部分自动加到左边，也就是：
print(max2(5, 6, 7))
#log: 10
#相当于：
args = (10, 5, 6, 7)
print(max(*args))

#log: 10