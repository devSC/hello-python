#coding=utf-8
import math

def my_abs(x):
    #类型转换
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')

    if x >= 0:
        return x
    else:
        return -x

#return None可以简写为return。

print(my_abs(120))

'''
空函数

如果想定义一个什么事也不做的空函数，可以用pass语句：
'''

def nop():
    pass
#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。

#pass还可以用在其他语句里，比如：

age = 10
if age >= 18:
    pass
#这里缺少了pass，代码运行就会有语法错误。


'''
返回多个值
'''

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print('x, y: ', x, y)
#log: x, y:  151.96152422706632 70.0

#这里返回的是个元组tuple, 语法上，返回一个tuple可以省略括号  然后做了解包
z = move(200, 100, 50)
print('z', z)
#log z (250.0, 100.0)


def add_end(L=[]):
    L.append('END')
    return L

'''
默认参数必须指向不变对象！
'''
add_end()
#['END']
add_end()
#['END', 'END']
add_end()
#['END', 'END', 'END']

'''
Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

So: 默认参数必须指向不变对象！
'''

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

'''
可变参数：

定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。


在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。
但是，调用该函数时，可以传入任意个参数，包括0个参数

'''
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

#0个参数
calc()

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：

nums = [1, 2, 3]
calc(nums[0], nums[1], nums[2])

'''
这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，

把list或tuple的元素变成可变参数传进去：
'''
nums = [1, 2, 3]
calc(*nums)

#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。


'''
关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。

而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
'''

def person(name, age, **kw):
    print('name:', name, 'age: ', age, 'other: ', kw);

person('Michael', 19)

person('Bob', 27, city='Beijing')

person('Bob', 27, city='Beijing', job='python')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}

#kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person('Jack', 10, **extra)



'''
命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于到底传入了哪些，就需要在函数内部通过kw检查。
'''
def newPerson(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age: ', age, 'other: ', kw);


'''
可以用命名关键字参数，限制关键字参数的名字

例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
'''

def person1(name, age, *, city='Beijing', job):
    print(name, age, city, job)

'''
关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
'''


person1('helu', 21, city='Xiian', job='php')


'''
如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
'''

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

'''
命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
'''
#person2('Jack', 24, 'Beijing', 'Engineer')
#error: TypeError: person2() missing 2 required keyword-only arguments: 'city' and 'job'


'''
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。

但参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

#*args 是可变参数 **kw 是关键字参数
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = {1, 2, 3, 4}
kw = {'d' : 99, 'x' : '#'}

f1(*args, **kw)
#log: a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}

'''
所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
'''



'''
递归函数
'''

def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(5))


'''
递归函数会造成 栈溢出

在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。

解决递归调用栈溢出的方法是通过尾递归优化，

事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。

但大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。
'''
# print(fact(1000)) 会造成栈溢出

def newFact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

newFact(5)
# newFact(1000)
#log: RecursionError: maximum recursion depth exceeded in comparison
