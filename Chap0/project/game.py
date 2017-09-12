# -*- coding: utf-8 
from random import randint

num = randint(0,20)
guess = int(input('请你输入一个数字:'))
n = 1
while n<10:

    if num < guess:
        print('你猜的数字大了！还有%d次机会哦！' % (10-n))
        n+=1
    elif guess<num:
        print('你猜的数字小了!还有%d次机会哦！' % (10-n))
        n+=1
    else:
        print('恭喜你，你猜了%d次，终于猜对了！' %(n))
        break
    guess = int(input('请你输入一个数字:'))   
    