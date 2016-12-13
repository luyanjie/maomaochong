#Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Tracy']
#变量classmates就是一个list。用len()函数可以获得list元素的个数：
print(len(classmates))
#用索引来访问list中每一个位置的元素，记得索引是从0开始的：
print(classmates[0]) #Michael
#如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：
print(classmates[-1]) # Tracy
#以此类推，可以获取倒数第2个、倒数第3个：

#list是一个可变的有序表，所以，可以往list中追加元素到末尾：
classmates.append("Adam")
classmates.insert(1,"Jack")
#要删除list末尾的元素，用pop()方法：
classmates.pop()
#要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
classmates.pop(1)
#要把某个元素替换成别的元素，可以直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
#list里面的元素的数据类型也可以不同，比如：
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']

#tuple
#另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

classmates = ('Michael', 'Bob', 'Tracy')
#现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。
#定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
#所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
#理论上tuple不可变，但是在一些特定的情况下可以变化（实际变的不是tuple）
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # ('a', 'b', ['X', 'Y'])

#表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，
#指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
#理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。


#练习：请用索引取出下面list的指定元素：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print("打印Apple：%s" % L[0][0])
print('打印Python: %s' % L[1][1])
print("打印Lisa: %s" % L[2][2])