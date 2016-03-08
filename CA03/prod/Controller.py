'''
Created on Nov 1, 2015

@author: Turtle
'''
class Controller(object):
    from CA02.prod.StarSensor import StarSensor
    from CA04.prod.SolarCollector import SolarCollector
    deviceObjects = []
    rate = 0
    environment = None
    def __init__(self):
        pass
    
    def initialize(self,architectureFile):
        from CA02.prod.Environment import Environment
        from CA03.prod.Device import Device
        from CA03.prod.Monitor import Monitor
        from CA04.prod.SolarCollector import SolarCollector
        if (len(architectureFile) < 5 or (architectureFile.lower().find(".xml") == -1) ):
            raise ValueError('Controller.initialize(): invalid file name or file extension')
            return self.deviceObjects
        from Architecture import Architecture
        returnList = []
        arch = Architecture(architectureFile)
        rate = arch.rate
        list = arch.getComponentDefinition()
        for i in list:
            test = 0
            if (i.get("component").lower() == "environment"):
                if (len(i.get("parms")) < 1):
                    raise ValueError("Controller.initialize(): Environment cannot be initialized with less than 1 argument")
                e = Environment()
                for p in i.get("parms"):
                    if (p.get("name") == "rotationalPeriod"):
                       e.setRotationalPeriod(p.get("value")) 
                    elif(p.get("name") == "startTime"):
                        e.setStartTime(p.get("value"))
                    elif(p.get("name") == "degredation"):
                        e.setDegredation(p.get("value"))
                    else:
                        raise ValueError("Controller.initialize(): Environment does not have the parameter",p.get("name"))
                self.environment = e
                test = 1
            if (i.get("component").lower() == "monitor"):
                m = Monitor()
                if (len(i.get("parms")) != 1):
                    raise ValueError("Controller.initialize(): Monitor cannot be initialized with more than 1 argument")
                if (i.get("parms")[0].get("name") == "logFile"):
                    m.initialize(i.get("parms")[0].get("value"))
                else:
                    raise ValueError("Controller.initialize(): Monitor does not have the parameter",i.get("parms")[0].get("name"))
                returnList.append(m)
                test = 1
            if (i.get("component").lower() == "starsensor"):
                if (len(i.get("parms")) != 2):
                    raise ValueError("Controller.initialize(): Star Sensor cannot be initialized without a field of view and a star file")
                for j in i.get("parms"):
                    componentTest = 0
                    if (j.get("name") == "fieldOfView"):
                        s = StarSensor(float(j.get("value")))
                        componentTest = 1
                    if (j.get("name") == "starFile"):
                        s.initializeSensor(j.get("value"))
                        componentTest = 1
                    if (componentTest == 0):
                        raise ValueError("Controller.initialize(): Star Sensor does not have a field called ", j.get("name"))
                returnList.append(s)
                test = 1
            if (i.get("component").lower() == "device"):
                if (len(i.get("parms")) != 0):
                    raise ValueError("Controller.initialize(): Device does not have the parameter",i.get("parms")[0].get("name"))
                d = Device()
                returnList.append(d)
                test = 1
            if (i.get("component").lower() == "solarcollector"):
                s = SolarCollector()
                returnList.append(s)
                test = 1
            if (test == 0):
                raise ValueError(i.get("component"), " Does not Exist")
        self.deviceObjects = returnList   
        return returnList
    def sunCheck(self):
        starSensor = None
        sc = None
        for x in self.deviceObjects:
            if isInstance(x, StarSensor):
                starSensor = x 
            if isInstance(x, SolarCollector):
                sc = x
        if (sc != None and starSensor != None ):
            sc.setStarSensor(starSensor)
    def run(self, microseconds):
        from CA02.prod.Environment import Environment
        from CA03.prod.Monitor import Monitor
        self.sunCheck()
        try: val = int(microseconds)
        except: raise ValueError('Controller.run(): invalid parameter')
        if (microseconds < 0):
            raise ValueError('Controller.run(): invalid parameter')
        booleanEnvTrue = 0
        if (self.environment != None):
            booleanEnvTrue = 1
        booleanMonTrue = 0
        for i in self.deviceObjects:
            if (isinstance(i, Monitor)):
                booleanMonTrue = 1
        if (booleanEnvTrue != 1 or booleanMonTrue != 1):
            raise ValueError("Controller.run(): the controller has not been properly initialized")
        simulatedTime = 0
        innerTime = 0;
        while (simulatedTime < microseconds):
            for i in self.deviceObjects:
                i.configure(self.environment)
                if (isinstance(i, Monitor)):
                    i.serviceRequest("Controller", "Monitor")
                else:
                    i.serviceRequest()
                    innerTime = innerTime + 40
                if (innerTime < self.rate):
                    i.environment.incrementTime(self.rate)            
            simulatedTime = simulatedTime + innerTime
            innerTime = 0     
        return simulatedTime        
        
        
        