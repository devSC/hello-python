#coding=utf-8

'''
list

Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
'''

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates: %s count: %d' % (classmates, len(classmates)))
print(classmates[0])

'''
如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

也就是倒出第一
'''
print(classmates[-1])

#追加元素
classmates.append('Adam')


classmates.insert(1, 'Jacl')


#list里面的元素的数据类型也可以不同，比如：

L = ['Apple', 123, True]


#list元素也可以是另一个list，比如：

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(len(s))
#log: 4


'''
tuple

另一种有序列表叫元组：tuple。
tuple和list非常类似，但是tuple一旦初始化就不能修改，

比如同样是列出同学的名字：
'''

tclassmates = ('Michael', 'Bob', 'Tracy')

print('tclassmates:', tclassmates);

#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)


'''
“可变的”tuple：
'''


t = ('a', 'b', ['A', 'B'])
print(t)
#log: A, B
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
#log: ('a', 'b', ['X', 'Y'])

#这里指向的是list元素, list元素本身没变, 但其内容可以变化
