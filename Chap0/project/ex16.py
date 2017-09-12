# -*- coding: utf-8 

from sys import argv 
script,filename = argv # 参数解包

print ("we're going to erase %r." % filename) 
print ("if you don't want that,hit CTRL-C (^C).")
print ("if you do want that,hit RETURN.")

input("?")

print ("opening the file...")
target = open(filename,'w') # 打开一个写文件并赋给target

print ('truncateing the file.goodbye!')
target.truncate() # 删除文件中的所有内容

print ("now i'm going to ask you for three lines.")

line1 = input("line1: ") # 输入内容并赋给line1
line2 = input('line2: ')
line3 = input('line3: ')

print ("i'm going to write this to the file.")

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print ("and finally,we close it.")
target.close()# 关闭文件




