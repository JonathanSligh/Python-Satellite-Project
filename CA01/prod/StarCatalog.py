'''
    Created on Aug 31, 2015
    @author: Jonathan Sligh (jrs0058)
'''
from collections import namedtuple
Star = namedtuple("Star", "identifier brightness ascension declination")
class StarCatalog(object):
    starList = []
    def __init__(self):
        pass
    
    def loadCatalog(self, starFile=None):
        tempStarList = []
        try: fFile = open(starFile)
        except: raise ValueError('StarCatalog.loadCatalog():  Invalid file name')
        for line in fFile:
            info = line.split()
            try:
                star = Star(identifier=float(info[0]), brightness=float(info[1]), ascension=float(info[2]), declination=float(info[3]))
            except:
                raise ValueError('StarCatalog.loadCatalog():  Invalid Star Input')
            duplicateTestStar = None
            duplicateTestStar = [item for item in tempStarList if item[0] == star[0]]
            if (duplicateTestStar == []):
                tempStarList.append(star)
            else:
                raise ValueError('StarCatalog.loadCatalog():  Duplicate Star')
        self.starList = tempStarList
        if (len(tempStarList) == None):
            return 0
        return len(tempStarList)
    
    def emptyCatalog(self):
        i = len(self.starList)
        self.starList[:] = []
        if (i == None):
            return 0
        return i
    
    def getStarCount(self, lowerMagnitude=None, upperMagnitude=None):
        if (lowerMagnitude == None and upperMagnitude == None):
            return len(self.starList)    
        try:
            if (lowerMagnitude != None):
                val = int(lowerMagnitude)
        except: raise ValueError("StarCatalog.getStarCount():  Lower Magnitude is not a number")
        
        try:
            if (upperMagnitude != None):
                val = int(upperMagnitude)
        except: raise ValueError("StarCatalog.getStarCount():  Upper Magnitude is not a number")
        if (lowerMagnitude != None and upperMagnitude != None):
            if (lowerMagnitude > upperMagnitude):
                raise ValueError("StarCatalog.getStarCount():  Lower Magnitude is larger than or equal to the Upper Magnitude")
        
        if(lowerMagnitude == None):
            lowerMagnitude = min(l[1] for l in self.starList)
        if (upperMagnitude == None):
                upperMagnitude = max(l[1] for l in self.starList)
                
        listInRange = [x for x, v in enumerate(self.starList) if v[1] >= lowerMagnitude and v[1] <= upperMagnitude]
        if (len(listInRange) == None):
            return 0
        return len(listInRange)
    
    def getMagnitude(self, rightAscensionCenterPoint=None,
                     declinationCenterPoint=None,
                     fieldOfView=None):
        import math
        if (rightAscensionCenterPoint < 0 or rightAscensionCenterPoint > 2 * math.pi):
            raise ValueError("StarCatalog.getMagnitude():  Right Ascension Center Point is out of bounds")
        
        if (declinationCenterPoint < -2 * math.pi or declinationCenterPoint > 2 * math.pi):
            raise ValueError("StarCatalog.getMagnitude():  Declination Center Point is out of bounds")
        
        if (fieldOfView < 0 and fieldOfView > 2 * math.pi):
            raise ValueError("StarCatalog.getMagnitude():  Field of View is out of bounds")
        listInRange = []
        for v in self.starList:
            if float(v[2]) >= (float(rightAscensionCenterPoint) - (fieldOfView / 2.0)) and float(v[2]) <= (float(rightAscensionCenterPoint) + (fieldOfView / 2.0)):
                if float(v[3]) <= (float(declinationCenterPoint) + (fieldOfView / 2.0)) and float(v[3]) >= (float(declinationCenterPoint) - (fieldOfView / 2.0)):
                    listInRange.append(v)
        brightestStar = 1.7976931348623157e+308
        for x in listInRange:
            if (float(x[1]) < float(brightestStar)):
                brightestStar = x[1]
        if (brightestStar == 1.7976931348623157e+308):
            return None
        return brightestStar