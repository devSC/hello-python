#!/usr/bin/env python3
#conding=utf-8

#表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
'a test module'

#__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
__author__ = 'Wilson'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print("Hello world")
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('To manay arguments!')

if __name__ == "__main__":
    test()



'''
作用域:

正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；

类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途，比如上面的__author__，__name__就是特殊变量，hello模块定义的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；

类似_xxx和__xxx这样的函数或变量就是非公开的（private），不应该被直接引用，比如_abc，__abc等；

从编程习惯上不应该引用private函数或变量。
'''


def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


'''
macOS下同时有python2和python3的时候

可以用python3 -m pip install pillow将模块指定安装到python3下。
'''

from PIL import Image
# im = Image.open('test.png')
# print(im.format, im.size, im.mode)

