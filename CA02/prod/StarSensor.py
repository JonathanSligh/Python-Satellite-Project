'''
Created on Oct 3, 2015

@author: Jonathan
'''
from Environment import Environment
from CA01.prod.StarCatalog import StarCatalog
class StarSensor(object):
    fieldOfView = 0;
    numOfMicroSecInDay = 89764100000
    starList = []
    environment = None
    def __init__(self, fov):
        try: self.fieldOfView = float(fov)
        except: raise ValueError('StarSensor.init():  invalid parameter for Field of View')
        import math
        if (fov > 0 and fov <= math.pi / 4):
            self.fieldOfView = fov
        else:
            raise ValueError('StarSensor.init():  invalid parameter for Field of View')
            pass
        
    def initializeSensor(self, starFile):
        s = StarCatalog()
        numStars = s.loadCatalog(starFile)
        self.starList = s.starList
        return numStars
    
    def configure(self, environment):
        isInstance = False
        try:
            environment.getTime()
            isInstance = True
        except:
            isInstance = False
        if isInstance:
            self.environment = environment
            return True
        else:
            raise ValueError('StarSensor.configure():  interface is invalid')
            return False
    
    def serviceRequest(self):
        magnitude = None
        if (self.environment == None):
            return None
        sensorRightA = self.getSensorPosition()[0]
        sensorDeclination = self.getSensorPosition()[1]
        s = StarCatalog()
        s.starList = self.starList
        magnitude = s.getMagnitude(sensorRightA, sensorDeclination, self.fieldOfView)
        if (magnitude == None):
            return None
        magnitude = magnitude * 10
        printMag = ''
        if (magnitude < 0):
            printMag = (hex(((abs(magnitude) ^ 0xffff) + 1) & 0xffff)[2:])
        else:
            printMag = (hex(magnitude)[2:])
        if (len(printMag) == 1):
            printMag = '000' + printMag
        elif(len(printMag) == 2):
            printMag = '00' + printMag
        elif(len(printMag) == 3):
            printMag = '0' + printMag        
        self.environment.incrementTime(40)
        return printMag
    
    def getSensorPosition(self):
        numList = []
        import math
        sensorRightA = 0
        sensorDecl = 0
        if (self.environment == None):
            raise ValueError("StarSensor.getSensorPosition: StarSensor's environment wasnt initialized")
        if (self.environment != None and self.environment.getRotationalPeriod() == None):
            raise ValueError("StarSensor.getSensorPosition: StarSensor's rotational period isnt initialized")
        if (self.environment.getTime() == 0):
            sensorRightA = math.pi / 2.0
            sensorDecl = 0
        else:
            timeRemainder = (float(self.environment.getTime()) / float(self.numOfMicroSecInDay))
            timeRemainder = float(str(timeRemainder).split('.')[1])
            timeRemainder2 = float(self.environment.getTime()) / float(self.environment.getRotationalPeriod())
            timeRemainder2 = float(str(timeRemainder2).split('.')[1])
            rightASat = 2.0 * math.pi*float(timeRemainder)
            sensorDecl = 2.0 * math.pi*float(timeRemainder2)
            if (sensorDecl >= -2*math.pi and sensorDecl <= 2.0*math.pi):
                sensorRightA = float(rightASat - math.pi/2.0)
            else:
                sensorRightA = float(rightASat + math.pi/2.0)
        numList.append(sensorRightA)
        numList.append(sensorDecl)
        return numList
    
    def isSunInView(self):
        from collections import namedtuple
        Star = namedtuple("Star", "identifier brightness ascension declination")
        sun = Star("10137", "-32768", "0", "0")
        self.starList.append(sun)
        s = StarCatalog()
        s.starList = self.starList
        if (float(s.getMagnitude(0,0, .5)) == -32768.0):
            return True
        else:
            return False
        
        
        
