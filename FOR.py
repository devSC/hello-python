#coding=utf-8

classmates = ['Michael', 'Bob', 'Tracy']

#for...in循环，
for name in classmates:
    print(name)


sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)


'''
range()函数，可以生成一个整数序列，
再通过list()函数可以转换为list。

比如range(5)生成的序列是从0开始小于5的整数：
'''

print(list(range(5)))


#range(101)就可以生成0-100的整数序列，计算如下：
sum = 0
for x in range(101):
    sum = sum + x
print(sum)

'''
while循环，只要条件满足，就不断循环，条件不满足时退出循环。

比如我们要计算100以内所有奇数之和，可以用while循环实现：
'''

sum = 0
n = 99

while n > 0:
    sum = sum + n
    n = n - 2
print(sum)


'''
break

在循环中，break语句可以提前退出循环。
'''

n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')



'''
continue

在循环过程中，也可以通过continue语句，跳过当前的这次循环，直接开始下一次循环。


如果我们想只打印奇数，可以用continue语句跳过某些循环：
'''
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)


