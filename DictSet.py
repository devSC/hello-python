#coding=utf-8

d = {'michael' : 96, 'bib' : 89, 'tracy' : 82}
print(d['michael'])

#存值
d['adam'] = 90

#避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
if 'Tomos' in d:
    print(d['Tomos'])
else:
    print('did\'t have \'Tomos\' key')
#dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Tomose', 1))


#删除key value同时也会被删除
d.pop('bib')



'''
set

set和dict类似，也是一组key的集合，但不存储value。

由于key不能重复，所以，在set中，没有重复的key。
'''

s = set([1, 2, 3])

print('s:', s)

#通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s.add(4)

s.remove(3)

