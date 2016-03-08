'''
Created on Aug 30, 2015

@author: Jonathan Sligh
'''
from CA01.prod.StarCatalog import StarCatalog

s = StarCatalog()
s.loadCatalog("star_file.txt")
print(s.getStarCount(0, 5))
print(s.getMagnitude(100, 11, 100))