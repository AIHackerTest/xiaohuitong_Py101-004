# -*- coding: utf-8 -*-

# 赋值语句
x = 'there are %d types of people.' % 10
binary = 'binary'
do_not = "don't"
y = 'those who know %s and those who %s .'% (binary,do_not) # 字符串包含字符串
# 打印x，y
print (x)
print (y)
# 把x所代表的句子赋给“r”，然后在打印出来
print ('i said:%r.' %x) # 字符串包含字符串
# 把y所代表的句子赋给“s”，然后在打印出来
print ("i also said:'%s'." %y) # 字符串包含字符串

# 赋值语句
hilarious = False
joke_evluation = "isn't that joke so funny?! %s"

# 把hilarious的值赋给"isn't that joke so funny?! %s"中的‘s’然后打印
print (joke_evluation % hilarious) # 字符串包含字符串
# 赋值语句
w = "this is the left side of ..."
e = 'a string with a right side .'

print (w+e)

