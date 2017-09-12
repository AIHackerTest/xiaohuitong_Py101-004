# -*- coding: utf-8 

from random import randint

print('''程序内部用0-9生成一个四位数，每个数位上的数字不能重复，且首位数字不能为0.
然后用户用10次机会对这个数字进行猜测，程序返回相应的提示。''')
while True:
    x = randint(1,9)
    y = randint(0,9)
    z = randint(0,9)
    w = randint(0,9)
    if (x!=y and x!=z and x!=w and y!=z and y!=w and z!=w):
        num = x*1000+y*100+z*10+w
        
        break

print(num)

num_str = str(num)

for i in range(10):
    guess_num = str(input('enter four numbers:'))
	
    a = 0
    b = 0
    if num_str!=guess_num:
        for j in range(4):
            if guess_num[j] == num_str[j]:
                a+=1
            elif guess_num[j] in num_str:
                b+=1
            else:
                pass
        print(a,'A',b,'B','你还有',9-i,'次机会')
    else:
        print('恭喜你，你回答了',i+1,'次，终于答对了')
        break
		






        
