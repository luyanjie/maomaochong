#字符串和编码
#在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
#在最新的Python 3版本中，字符串是以Unicode编码的，也就是说，Python的字符串支持多语言，例如：
print('包含中文的str')
#对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符：
print(ord('A')) #65
print(ord('中')) #20013
print(chr(66)) #'A'
print(chr(25991)) #'文'
#如果知道字符的整数编码，还可以用十六进制这么写str：
print('\u4e2d\u6587') # '中文'
#由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
#Python对bytes类型的数据用带b前缀的单引号或双引号表示：
#要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
#以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如：
print('ABC'.encode('ascii'))  #b'ABC'
print('中文'.encode('utf-8')) #b'\xe4\xb8\xad\xe6\x96\x87'
#反过来，如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
print(b'ABC'.decode('ascii')) #'ABC'
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')) #'中文'
print('要计算str包含多少个字符，可以用len()函数：')
print(len('sfsdfs'))
#可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。

#最后一个常见的问题是如何输出格式化的字符串。我们经常会输出类似'亲爱的xxx你好！你xx月的话费是xx，余额是xx'之类的字符串，而xxx的内容都是根据变量变化的，所以，需要一种简便的格式化字符串的方式。
print('Hello, %s' % 'world')  # Hello world
print('Hi, %s, you have $%d.' % ('Michael', 1000000)) # 'Hi, Michael, you have $1000000.'

print('常见的占位符有：%d（整数）  %f(浮点数)  %s(字符串) %x(十六进制整数)')
#其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d'%(3,1))  #  3-01
print('%.2f' % 3.1415926) #3.14

#练习：小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
r = (85-72)/72*100
print('%.1f%%' % r)  #用%%来表示一个%