'''
Created on Oct 3, 2015

@author: Jonathan
'''
x = int(1)
if (x < 0):
    print (hex(((abs(x) ^ 0xffff) + 1) & 0xffff)[2:])
else:
    print(hex(x)[2:])
    print('000' + hex(x)[2:])