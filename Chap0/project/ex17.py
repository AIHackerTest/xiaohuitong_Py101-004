# -*- coding: utf-8 

from sys import argv
from os.path import exists

script,from_file,to_file = argv

print ("copying from %s to %s" % (from_file,to_file))

# we could do these two on line on line too,how?
in_file = open(from_file)
indata = in_file.read()

print ("the input file is %d bytes long" % len(indata))
print ("dose the output file exist? %r" % exists(to_file))
print ('ready,hit enturn to continue,ctrl-c to abort.')
input()

out_file = open(to_file,'w')
out_file.write(indata)

print ("alright,all done")

out_file.close()
in_file.close()


