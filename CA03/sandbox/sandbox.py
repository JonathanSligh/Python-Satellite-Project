'''
Created on Nov 1, 2015

@author: Turtle
'''
hexnum = ""
num = 32767
if (num >= 0):
    hexnum = hex(num)[2:]
else:
    hexnum = hex(((abs(num) ^ 0xffff)) & 0xffff)[2:]    
print(hexnum)

val = "hi.tt"
if (val.find(".txt")):
    print("IT FUCKINGWORKS")
    print (len(val))