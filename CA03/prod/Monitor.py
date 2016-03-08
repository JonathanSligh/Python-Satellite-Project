'''
Created on Nov 1, 2015

@author: Turtle
'''
class Monitor(object):
    logFile = ""
    environment = None
    def __init__(self):
        pass
    
    def initialize(self, logFile):
        if ((len(logFile) < 5) or (logFile.lower().find(".txt") == -1)):
            raise ValueError('Monitor.initialize(): invalid file name or file extension')
        self.logFile = logFile
        import os.path
        return not os.path.isfile(logFile)
    
    def configure(self, environment):
        from CA02.prod.Environment import Environment
        if (isinstance(environment, Environment)):
            self.environment = environment
            return True
        else:
            raise ValueError('Monitor.configure(): invalid instance of environment')
    
    def serviceRequest(self, source, target, event = None):
        from CA02.prod.Environment import Environment
        if (self.environment != None and self.logFile != ""):
            if (event == None):
                event = "serviceRequest"
            text = str(self.environment.getTime()) + "\t" + source + "\t" + target + "\t" + event
            myFile = open(self.logFile, 'w+')
            myFile.write(text)
            return self.environment.getTime()
        else:
            raise ValueError("Monitor.serviceRequest(): the monitor has not been initialized correctly ")
        
        
         