#!/usr/bin/env python3
#声明支持中文
# -*- coding: utf-8 -*-
#或者
#coding=utf-8

print('hello world')

#print()函数也可以接受多个字符串，用逗号“,”隔开，就可以连成一串输出：
print('The quick brown fox', 'jumps over', 'the lazy dog')
#print()会依次打印每个字符串，遇到逗号“,”会输出一个空格，因此，输出的字符串是这样拼起来的：

print('100 + 200 =', 100 + 200)

#输入
#name = input('please enter your name: ');
#print('name: ', name);


a = 100
if a >= 0:
    print(a)
else:
    print(-a)


#Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print('\\\t\\')

print(r'\\\t\\')

#允许用'''...'''的格式表示多行内容
print('''line1
... line2
... line3''')

True
False

#空值
None

a = 'Abc'
b = a

#常量
#通常用全部大写的变量名表示常量：
TI = 3.1415936


'''
字符串和编码
https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431664106267f12e9bef7ee14cf6a8776a479bdec9b9000
'''

#ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A')

ord('直')


#编码
print('中文'.encode('utf-8'))
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
#log: b'\xe4\xb8\xad\xe6\x96\x87'

#格式化

print('Hello, %s' % 'world')
#log: 'Hello, world'
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
#log: 'Hi, Michael, you have $1000000.'

#%s会把任何数据类型转换为字符串
print('Age: %s. Gender: %s' % (25, True))
#log: Age: 25. Gender: True





