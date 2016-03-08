'''
Created on Nov 30, 2015

@author: Turtle
'''
class SolarCollector(object):
    environment = None
    starSensor = None
    def __init__(self):
        pass
    def setStarSensor(self, starSensor):
        self.starSensor = starSensor
    def configure(self, environment):
        from CA02.prod.Environment import Environment
        if (isinstance(environment, Environment)):
            self.environment = environment
            return True
        else:
            raise ValueError('SolarCollector.configure(): invalid instance of environment')
    def serviceRequest(self):
        if (self.environment == None):
            raise ValueError('SolarCollector.serviceRequest(): SolarCollector has not been correctly configured with an environment')
        if self.starSensor.isSunInView():
            return 0x7FFF*((100 - self.environment.getDegredation())*.01);
        return 0x0000