#coding=utf-8

age = 3

#后面有 冒号 :
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')


'''
if <条件判断1>:
    <执行1>
elif <条件判断2>:
    <执行2>
elif <条件判断3>:
    <执行3>
else:
    <执行4>
'''

'''
再议 input

最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：
'''


#input 返回的结果是str , 这里需要转为int
birth = input('birth: ')
if int(birth) < 2000:
    print('00前')
else:
    print('00后')