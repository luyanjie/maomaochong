#条件判断
age = 3
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

#if判断条件还可以简写，比如写：
x = True
if x:
    print('Ture')

#最后看一个有问题的条件判断。很多同学会用input()读取用户的输入，这样可以自己输入，程序运行得更有意思：
#birth = input('birth: ')
#if birth < 2000:
#    print('00前')
#else:
#    print('00后')

#输入1982，结果报错： 这是因为input()返回的数据类型是str，str不能直接和整数比较，必须先把str转换成整数。Python提供了int()函数来完成这件事情：
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')

#int()函数发现一个字符串并不是合法的数字时就会报错，程序就退出了。

#练习：小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

h = 1.75
g = 80.5
BMI = g/(h*h)
if BMI>1:
    print(True)
else:
    print(False)