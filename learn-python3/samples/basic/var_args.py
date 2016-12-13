# 方法参数可以设置默认值，以下求x参数的n次方就是当不传n参数时，自动复制为2 
def power(x,n=2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

print(power(2))
print(power(2,2))
#两者的结果是一样的  都为4
#需要注意几点
#1：必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）； 
#2：如何设置默认参数。当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)

enroll("jokin","5",city='XiaMen')#多个默认参数时  可以指定默认参数

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def hello(greeting, *args):
    if (len(args)==0):
        print('%s!' % greeting)
    else:
        print('%s, %s!' % (greeting, ', '.join(args)))

hello('Hi') # => greeting='Hi', args=()
hello('Hi', 'Sarah') # => greeting='Hi', args=('Sarah')
hello('Hello', 'Michael', 'Bob', 'Adam') # => greeting='Hello', args=('Michael', 'Bob', 'Adam')

names = ('Bart', 'Lisa')
hello('Hello', *names) # => greeting='Hello', args=('Bart', 'Lisa')