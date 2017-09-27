#coding=utf-8

#serialization demo

__author__ = 'Wilson'


d = dict(name='bob', age=20, score=88)

#Python提供了pickle模块来实现序列化。
import pickle

print(pickle.dumps(d))

'''
pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。

或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
'''

f = open('dump.text', 'wb')
pickle.dump(d, f)
f.close()
#log: b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x03\x00\x00\x00bobq\x02X\x03\x00\x00\x00ageq\x03K\x14X\x05\x00\x00\x00scoreq\x04KXu.'

'''
读取时:

文件->bytes->对象
'''
f = open('dump.text', 'rb')

#bytes->对象
d = pickle.load(f)
f.close()
print(d)
#log: {'name': 'bob', 'age': 20, 'score': 88}

'''
目前Pickle保存那些不重要的数据，版本兼容可能会有问题
'''


'''
JSON

JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
'''

import json

#对象->json
print(json.dumps(d))
#log: {"name": "bob", "age": 20, "score": 88}
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
#log: {'age': 20, 'score': 88, 'name': 'Bob'}


'''
JSON 序列化 class
'''
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
# print(json.dumps(s)) #log: TypeError: Object of type 'Student' is not JSON serializable

#序列化Student需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name' : std.name,
        'age' : std.age,
        'score' : std.score
    }


print(json.dumps(s, default=student2dict))
#log: {"name": "Bob", "age": 20, "score": 88}

#一般情况下下面声明可以将任意class的实例变为dict：
print(json.dumps(s, default=lambda obj: obj.__dict__)) #__dict__ 为class属性

#因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


'''
反序列化
'''

#需要传入的object_hook函数负责把dict转换为Student实例：
def dic2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dic2student))
#log: <__main__.Student object at 0x104544470>



'''
优先使用JSON.

序列化更通用、更符合Web标准
'''