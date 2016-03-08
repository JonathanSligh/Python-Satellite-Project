'''
Created on Nov 1, 2015

@author: Turtle
'''
class Device(object):
    environment = None
    def __init__(self):
        pass
    
    def configure(self, environment):
        from CA02.prod.Environment import Environment
        if (isinstance(environment, Environment)):
            self.environment = environment
            return True
        else:
            raise ValueError('Device.configure(): invalid instance of environment')
    
    def serviceRequest(self):
        from CA02.prod.Environment import Environment
        if (self.environment == None):
            raise ValueError('Device.serviceRequest(): configure() has not yet been called')
        from random import randint
        from random import uniform 
        posNums = randint(1, 32767)
        negNums = randint(-32767, -1)
        percent = uniform(0.0, 1.0)
        num = 0
        if (percent <= .25):
            num = 0
        if (percent <= .75 and percent > .25):
            num = posNums
        if (percent > .75):
            num = negNums
        self.environment.incrementTime(40)
        hexnum = ""
        if (num >= 0):
            hexnum = hex(num)[2:]
        else:
            hexnum = hex(((abs(num) ^ 0xffff)) & 0xffff)[2:]    
        return hexnum