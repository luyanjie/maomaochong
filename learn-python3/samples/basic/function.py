#调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
#如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
abs(-1992)
#取最大值
max(1,2,3)
min(1,2,3)
#数据类型转换
int('123')
float('12.34')
str(1.222)
bool(1)
#函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs
print(a(-1))

#请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
h1 = 255
h2 = 1000
print(hex(h1),hex(h2))

##定义函数
#定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
#我们以自定义一个求绝对值的my_abs函数为例：
def my_abs(x):
    if x>=0:
        return x
    else:
        return -x

c = my_abs(-3)
print(c)

#空函数
def nop():
    pass

#pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
#当传入了不恰当的参数时，内置函数abs会检查出参数错误，而我们定义的my_abs没有参数检查，会导致if语句出错，出错信息和abs不一样。所以，这个函数定义不够完善。
#让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：

#返回多个值
import math

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

#import math语句表示导入math包，并允许后续代码引用math包里的sin、cos等函数。
#但其实这只是一种假象，Python函数返回的仍然是单一值：
r = move(100, 100, 60, math.pi / 6)
print(r) #(151.96152422706632, 70.0)

#原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

#函数的参数
#Python的函数定义非常简单，但灵活度却非常大。除了正常定义的必选参数外，还可以使用默认参数、可变参数和关键字参数，使得函数定义出来的接口，不但能处理复杂的参数，还可以简化调用者的代码
#我们先写一个计算x2的函数：

def power(x):
    return x*x
#当我们调用power函数时，必须传入有且仅有的一个参数x：
#如果要加参数(n的默认值是2  可以传也可以不传) 默认参数方法
def power2(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
#存在多个默认参数的时候（默认参数可以按顺序也可以不按顺序）
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

#比如：
enroll('Bob', 'M', 7) #按顺序
enroll('Adam', 'M', city='Tianjin') #不按顺序

#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下：
#先定义一个函数，传入一个list，添加一个END再返回：
def add_end(L=[]):
    L.append('END')
    return L
#当正常条用的时候
add_end([1, 2, 3]) #[1, 2, 3, 'END']
add_end(['x', 'y', 'z']) #['x', 'y', 'z', 'END']
#当你使用默认参数调用时，一开始结果也是对的：
add_end() #['END']
#但是，再次调用add_end()时，结果就不对了：
add_end() #['END', 'END']
add_end() #['END', 'END', 'END']

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
#所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
#要修改上面的例子，我们可以用None这个不变对象来实现：

def add_endtest(L=None):
    if L is None:
        L = []
    L.append("END")
    return L

#add_endtest() 无论调用多少次都是 ['END']
#为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。
#可变参数:在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

calc([1, 2, 3])
calc((1, 3, 5, 7))
#如果利用可变参数，调用函数的方式可以简化成这样：
calctest(1, 2, 3)
calctest(1, 3, 5, 7)

def calctest(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
nums = [1, 2, 3]
calctest(nums[0],nums[1],nums[2])
#这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1, 2, 3]
calctest(*nums)

#关键字参数
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数：
person("jokin",6)  #name: jokin age: 6 other: {}
#也可以传入任意个数的关键字参数：
person('Bob', 35, city='Beijing') #name: Bob age: 35 other: {'city': 'Beijing'}
person('Adam', 45, gender='M', job='Engineer') # name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('jack',24,city=extra['city'],job = extra['job']) #name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#上面的可以简化书写
person('jack',24,**extra) #name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra

#命名关键字参数
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person2(name, age, *, city, job):
    print(name, age, city, job)
#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person2('Jack', 24, city='Beijing', job='Engineer') #Jack 24 Beijing Engineer

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)
#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
#a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
#a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
#a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
#a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}

#Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！
#要注意定义可变参数和关键字参数的语法：
#*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。
#以及调用函数时如何传入可变参数和关键字参数的语法：
#可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。