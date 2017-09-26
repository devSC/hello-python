#coding=utf-8

#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431756919644a792ee4ead724ef7afab3f7f771b04f5000

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

'''
slice

取前3个元素，用一行代码就可以完成切片：
'''
print(L[0:3])

'''
L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。


如果第一个索引是0，还可以省略：
'''
print(L[:3])


'''
它同样支持倒数切片
'''

print(L[-2:])

M = list(range(100))

#取前10个每2个取一个：
print(M[:10:2])
'''
每5个取一个：
'''
print(M[::5])


'''
tuple 

tuple也可以用切片操作，只是操作的结果仍是tuple：
'''
T = (0, 1, 2, 3, 4, 5)

print("T: ", T[:3])


'''
遍历


'''
from collections import Iterable

if isinstance('abc', Iterable):
    print("abc 可遍历")
else:
    print('abc 不可遍历')


'''
Python内置的enumerate函数可以把一个list变成索引-元素对，
'''

for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)



'''
列表生成式

即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
'''

X = [x * x for x in range(1, 11) if x % 2 == 0]
print(X)
#log: [4, 16, 36, 64, 100]

'''
还可以使用两层循环，可以生成全排列：
'''

X = [m + n for m in 'ABC' for n in 'XYZ']
print(X)
#log: ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

'''
列出当前目录下的所有文件和目录名，可以通过一行代码实现：
'''

import os

print([d for d in os.listdir('.')]) # os.listdir可以列出文件和目录
#log: ['.DS_Store', 'HighFeature.py', 'ListTuple.py', 'FOR.py', 'HelloWorld.py', '.git', 'DictSet.py', 'Function.py', '.idea', 'IF.py']



'''
生成器

在Python中，一边循环一边计算的机制，称为生成器：generator。
目的: ，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。


列表生成式: 将[]改成()，就创建了一个generator：
'''
L = [x * x for x in range(10)]
print(L)
#log: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

g = (x * x for x in range(10))
print(g)
#log: <generator object <genexpr> at 0x104ad0f10>

'''
可以通过next()函数获得generator的下一个返回值：
'''
print(next(g))

#使用 for 循环 取generator中的值
for n in g:
    print(n)


#斐波拉契数列
def fib(max):
    n, a, b = 0, 0, 1

    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

    return 'done'

'''
这里 a, b = b, a + b 相当于: (a, b) = (b, a + b)

也就是:
t = (b, a + b) # t是一个tuple
a = t[0]
b = t[1]
'''

print("\n斐波拉契数列: ")
fib(10)


'''
可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。

也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
'''
def yfib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1

    return 'done'

'''
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
'''
print(yfib(6))

'''
这里enerator和函数的执行流程不一样。

函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
'''


#定义一个generator，依次返回数字1，3，5：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)


o = odd()
next(o)
#log: step 1
next(o)
#log: step 2
next(o)
#log: step 3

#遇到yield就中断，下次又继续执行


'''
用for循环取值
'''
for n in fib(10):
    print(n)


'''
拿到generator中 return 语句的返回值
'''

g = yfib(2)
while True:
    try:
        x = next(g)
        print('g: ', x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break
#log:
#g:  1
#g:  1
#Generator return value:  done


