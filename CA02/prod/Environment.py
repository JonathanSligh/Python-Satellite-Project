'''
Created on Oct 3, 2015

@author: Jonathan
'''
class Environment(object):
    simClock = 0
    degredation = 0
    rotatonalPeriod = None
    def __init__(self):
        self.simClock = 0
    
    def setStartTime(self, startTime):
        try: i = int(startTime)
        except: raise ValueError('Environment.setStartTime(): invalid parameter for startTime')
        if (startTime >= 0):
            self.simClock = startTime
            return startTime
        else:
            raise ValueError('Environment.setStartTime(): parameter does not fall in range') 
        
    def getTime(self):
        return self.simClock
    
    def incrementTime(self, microseconds):
        try: i = int(microseconds)
        except: raise ValueError('Environment.incrementTime():  invalid parameter for time to be incremented')
        if (microseconds >= 0):
            self.simClock += self.simClock + microseconds
        else:
            raise ValueError('Environment.incrementTime():  invalid bounds for time to add')
        return self.simClock
    
    def setRotationalPeriod(self, microseconds):
        try: i = int(microseconds)
        except: raise ValueError('Environment.setRotaionalPeriod:  invalid parameter for rotational period')
        if (microseconds >= 1000000):
            self.rotatonalPeriod = microseconds
            return microseconds
        else:
            raise ValueError('Environment.setRotationalPeriod():  parameter does not fall in range')
    
    def getRotationalPeriod(self):
        if (self.rotatonalPeriod == None):
            raise ValueError('Environment.getRotationalPeriod():  rotational period has not initially been set')
            pass
        else:
            return self.rotatonalPeriod
    
    def getDegredation(self):
        return self.degredation
    
    def setDegredation(self, degredation):
        try: i = int(degredation)
        except: raise ValueError('Environment.setDegredation(): invalid parameter for degredation')
        if (degredation >= 0 and degredation <= 100):
            self.degredation = degredation
            return degredation
        else:
            raise ValueError('Environment.setDegredation(): parameter does not fall in range')      
    
    
        
        