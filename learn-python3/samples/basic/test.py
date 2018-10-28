#打印输出
print(110+100)
print(110+102)
#Python的语法比较简单，采用缩进方式，写出来的代码就像下面的样子：
# 当语句以冒号:结尾时，缩进的语句视为代码块
#缩进有利有弊。好处是强迫你写出格式化的代码，但没有规定缩进是几个空格还是Tab。按照约定俗成的管理，应该始终坚持使用4个空格的缩进。
#缩进的另一个好处是强迫你写出缩进较少的代码，你会倾向于把一段很长的代码拆分成若干函数，从而得到缩进较少的代码。
#缩进的坏处就是“复制－粘贴”功能失效了，这是最坑爹的地方。当你重构代码时，粘贴过去的代码必须重新检查缩进是否正确。此外，IDE很难像格式化Java代码那样格式化Python代码。
#最后，请务必注意，Python程序是大小写敏感的，如果写错了大小写，程序会报错。
a = 100 
if a>=0:
    print(a)
else:
    print(-a)

#数据类型与变量
#整数  十进制例如：1，100，-8080，0，等等。 十六进制例如：用0x前缀和0-9，a-f表示，例如：0xff00，0xa5b4c3d2，等等。

#浮点数 浮点数也就是小数，之所以称为浮点数，是因为按照科学记数法表示时，一个浮点数的小数点位置是可变的，比如，1.23x109和12.3x108是完全相等的。浮点数可以用数学写法，如1.23，3.14，-9.01，等等。
#但是对于很大或很小的浮点数，就必须用科学计数法表示，把10用e替代，1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5，等等
#整数和浮点数在计算机内部存储的方式是不同的，整数运算永远是精确的（除法难道也是精确的？是的！），而浮点数运算则可能会有四舍五入的误差。
#
#字符串：

b = 'I\'M \"OK\"!'
print(b)
#表示的字符串内容是： I'm "OK"!
#转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\，可以在Python的交互式命令行用print()打印字符串看看：
#如果字符串里面有很多字符都需要转义，就需要加很多\，为了简化，Python还允许用r''表示''内部的字符串默认不转义，可以自己试试：
print(r'\\\t\\')
#如果字符串内部有很多换行，用\n写在一行里不好阅读，为了简化，Python允许用'''...'''的格式表示多行内容，可以自己试试：
print('''line1
... line2
... line3''')
print('''line1
line2
line3''')
#多行字符串'''...'''还可以在前面加上r使用
print(r'''line1
line2
line3''')

#布尔值
print(True)
print(False)
print(3>2)
print(3>5)
#布尔值可以用and、or和not运算。
print(True and False)
print(not True)

#空值 ：空值是Python里一个特殊的值，用None表示。None不能理解为0，因为0是有意义的，而None是一个特殊的空值。
#变量：变量的概念基本上和初中代数的方程变量是一致的，只是在计算机程序中，变量不仅可以是数字，还可以是任意数据类型。
# 在Python中，等号=是赋值语句，可以把任意数据类型赋值给变量，同一个变量可以反复赋值，而且可以是不同类型的变量，例如：
c = 123 # c是整数
print(c)
c = 'ABC' # c变为字符串
print(c)
#这种变量本身类型不固定的语言称之为动态语言，与之对应的是静态语言。静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。例如Java是静态语言

#常量
#所谓常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359
#但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，用全部大写的变量名表示常量只是一个习惯上的用法，如果你一定要改变变量PI的值，也没人能拦住你。
#/除法计算结果是浮点数，即使是两个整数恰好整除，结果也是浮点数：
print(9/3)  #3.0
#还有一种除法是//，称为地板除，两个整数的除法仍然是整数：
print(10 // 3) # 3
print(10 % 3) #1