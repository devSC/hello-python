#coding=utf-8

'Object oriented programming'

__author__ = "Wilson"


'''
类名通常是大写开头的单词

语法:
class 类名 (父类):

object 为所有对象的 父类.
'''
class Student(object):

    '''
    参数 self 表示实例本身,
    '''
    def __init__(self, name, score):

        #实例的变量名如果以__开头，就变成了一个私有变量（private）
        self.name = name

        #__name变量会被Python解释器自动改成 _Student__name
        self.__score = score

    def print_score(self):
        print('student name: %s score: %s' % (self.name, self.__score))

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'


bart = Student('Bart spart', 60)
bart.name = 'Bart'
print(bart.name)

def print_score(std):
    print('student name: %s score: %s' % (std.name, std.score))

#print_score(bart)
bart.print_score()


#_name，这样的实例变量外部是可以访问的, 但, 约定为私有的, 不要随意访问.
#变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名


'''
继承
'''

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')

class Cat(Animal):

    #覆盖父类方法
    def run(self):
        print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()

#判断一个变量是否是某个类型可以用isinstance()判断：

print(isinstance(dog, Dog))
#log: true
print(isinstance(dog, Animal))
#log: true

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(dog)
run_twice(cat)



class Timer(object):
    def run(self):
        print('Start...')

timer = Timer()


#动态语言的“鸭子类型”，它并不要求严格的继承体系，一个对象只要“看起来像鸭子，走起路来像鸭子”，那它就可以被看做是鸭子。 这里有点类似于Protocol
run_twice(timer)


'''
获取对象信息
'''

#判断对象类型
print(type(dog))
#log: <class '__main__.Dog'>



#type()函数返回的是什么类型呢？它返回对应的Class类型
print(type(123)==type(456))
#log: True



#判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import types
def fn():
    pass

print(type(fn)==types.FunctionType)
#log: True
print(type(abs)==types.BuiltinFunctionType)
#log: True
print(type(lambda x: x)==types.LambdaType)
#log: True
print(type((x for x in range(10)))==types.GeneratorType)
#log: True


'''
获得一个对象的所有属性和方法，可以使用dir()函数，

它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
'''

print(dir('ABC'))
#['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


'''
实例属性和类属性


Python是动态语言，根据类创建的实例可以任意绑定属性。

给实例绑定属性的方法是通过实例变量，或者通过self变量：
'''

print('hahahh')
class Student(object):
    name = 'Student' #类属性

    def __init__(self, name):
        self.name = name

s = Student('spasa')
print(s.name, Student.name)


#动态给实例绑定一个方法
def set_age(self, age):
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(25)
print('s.age: ', s.age)



def set_score(self, score):
    self.score = score

#为了给所有实例都绑定方法，可以给class绑定方法：
Student.set_score = set_score

s.set_score(100)

print('s.score: ', s.score)

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。



'''
使用__slots__ (中文:插槽)


限制该class实例能添加的属性

'''

class Student(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

s = Student()


#s.score = 100 #AttributeError: 'Student' object has no attribute 'score'


#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class GraduenteStudent(Student):
    #子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
    __slots__ = ('year')


s = GraduenteStudent()
#s.score = 100 error


'''
使用@property

@property装饰器就是负责把一个方法变成属性调用的：
'''

class Student(object):

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100 !')

        self.__score = value;

    #只定义getter方法，不定义setter方法就是一个只读属性：
    @property
    def year(self):
        return 2017


s = Student()
s.score = 60
print(s.score, s.year)



'''
多重继承

'''

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')



# 各种动物:
class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

'''
MixIn

在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。

MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。
'''

class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')



# 各种动物:
class Dog(Mammal, RunnableMixIn, FlyableMixIn):
    pass

class Bat(Mammal, FlyableMixIn):
    pass


#MixIn的目的就是给一个类增加多个功能，这样，在设计类的时候，我们优先考虑通过多重继承来组合多个MixIn的功能，而不是设计多层次的复杂的继承关系。

#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。




'''
定制类

'''

#__str__
class Student(object):
    def __init__(self, name):
        self.__name = name

    def __str__(self): #类似于swift中的 descriptionable protocol
        return 'Student object (name: %s)' % self.name

    #__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
    __repr__ = __str__



'''
__iter__

如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，
'''

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己


    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 10: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值

    #要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
    def __getitem__(self, n):
        if isinstance(n, int):  # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):  # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

        '''
        __getattr__
        
        __getattr__()方法，动态返回没有定义的一个属性 或 方法
        
        '''
    def __getattr__(self, item):
        print('__getattr__: ', item)
        if item == 'score':
            return 99
        if item == 'age':
            return lambda: 25

        #只返回特意的几个属性, 其他直接抛出错误.
        raise AttributeError('\'Fib\' object has no attribute \'%s\'' % attr)


f = Fib()
for n in f:
    print('fib: ', n)

print(f[10])

print(f.score)

print(f.age())


'''
这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。

这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。

举个例子：

现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：

http://api.server/user/friends
http://api.server/user/timeline/list
如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。

利用完全动态的__getattr__，我们可以写出一个链式调用
'''

class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__



print(Chain().status.user.timeline.list)
#log: /status/user/timeline/list


'''
__call__


任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
'''

class Student(object):
    def __init__(self, name):
        self.name = name

    #__call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
    def __call__(self):
        print('My name is %s.' % self.name)

s = Student('Michael')
#判断一个对象是否能被调用，能被调用的对象就是一个Callable对象
if callable(s):
    s()


'''
枚举

emum
'''

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))


#这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：
# print(Month.jan)
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
'''
log:
Jan => Month.Jan , 1
Feb => Month.Feb , 2
Mar => Month.Mar , 3
Apr => Month.Apr , 4
May => Month.May , 5
Jun => Month.Jun , 6
Jul => Month.Jul , 7
Aug => Month.Aug , 8
Sep => Month.Sep , 9
Oct => Month.Oct , 10
Nov => Month.Nov , 11
Dec => Month.Dec , 12
'''
#value属性则是自动赋给成员的int常量，默认从1开始计数。


#如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

from enum import unique

@unique #@unique装饰器可以帮助我们检查保证没有重复值。
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

#访问:

print(Weekday.Mon)
#log: Weekday.Mon
print(Weekday['Mon'])
#log: Weekday.Mon
print(Weekday.Mon.value)
#log: 1
print(Weekday(1))
#log: Weekday.Mon
print(Weekday.Mon == Weekday(1))
#log: true

#Enum可以把一组相关常量定义在一个class中，且class不可变，而且成员可以直接比较。


'''
使用元类

type()

动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
'''

print(type(Student))
#log: <class 'type'>

print(type(s))
#log: <class '__main__.Student'>

#type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：

def fn(self, name = 'world'): #定义函数
    print('Hello, ', name)

Hello = type('Hello', (object,), dict(hello=fn)) #创建 hello class
h = Hello()
h.hello()
#log: Hello,  world
print(type(h))
#log: <class '__main__.Hello'>

'''
要创建一个class对象，type()函数依次传入3个参数：

class的名称；
继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
'''

'''
metaclass


metaclass，直译为元类，简单的解释就是：

当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
'''

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaClass(type):
    def __new__(cls, name, bases, attrs):

        #添加add 方法
        attrs['add'] = lambda self, value: self.append(value)
        '''
        __new__()方法接收到的参数依次是：
            当前准备创建的类的对象；
            类的名字；
            类继承的父类集合；
            类的方法集合。
        '''
        return type.__new__(cls, name, bases, attrs)


#传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyLis时，要通过ListMetaclass.__new__()来创建
class MyList(list, metaclass=ListMetaClass):
    pass

L = MyList()
L.add(1) #给自定义的list添加了 add 方法.
print(L)

'''
ORM

ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。

要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
'''

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

#在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：

class StringField(Field):
    def __init__(self, name):
        #super() 为python3中写法
        super().__init__(name, 'varchar(100)')


class IntegerField(Field):
    def __init__(self, name):
        super().__init__(name, 'varchar(100)')



class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()

        for k, v in attrs.items():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))

        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s'% str(args))




class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

# 创建一个实例：
u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
# 保存到数据库：

#不到100行代码，我们就通过metaclass实现了一个精简的ORM框架。
u.save()


