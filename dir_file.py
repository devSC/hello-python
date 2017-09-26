#coding=utf-8

import os

print(os.name, os.uname())

print(os.environ)


#操作文件和目录

print(os.path.abspath('.'))

#log:/Users/devSC/Documents/MyProject/hello-python

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
# os.path.join('/Users/michael', 'testdir')
# '/Users/michael/testdir'
# 然后创建一个目录:
# os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
# os.rmdir('/Users/michael/testdir')


#要列出所有的.py文件，也只需一行代码：
files = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']

print(files)