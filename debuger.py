#coding=utf-8

'''
Debugger

'''

__author__ = 'Wilson'

'''
断言

凡是用print()来辅助查看的地方，都可以用断言（assert）来替代：

启动Python解释器时可以用-O参数来关闭assert：
'''
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

#foo(0) #log: AssertionError: n is zero!
print(foo(1))


'''
logging

把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
'''

import logging
logging.basicConfig(level=logging.DEBUG)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10/n)

