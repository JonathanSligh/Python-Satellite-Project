'''
Created on Oct 4, 2015

@author: Jonathan
'''
from CA02.prod import Environment
from CA02.prod import StarSensor
class Test():
    def test_1_StarSensor_init(self):
        s = StarSensor(.1)
        if (s.fieldOfView == .1):
            print('Test 1.1 Starsensor.init(): Normal init PASSED')
        else:
            print('Test 1.1 Starsensor.init(): Normal init FAILED')
        try:
            s = StarSensor(0)
            print('Test 1.2 StarSensor.init() Init raised exception when 0 FAILED')
        except:
            print('Test 1.2 StarSensor.init() Init raised exception when 0 PASSED')
        try:
            s = StarSensor('hi')
            print('Test 1.3 StarSensor.init() Init raised exception when string FAILED')
        except:
            print('Test 1.3 StarSensor.init() Init raised exception when string PASSED')
    def test_2_StarSensor_initializeSensor(self):
        s = StarSensor(.1)
        try:
            s.initializeSensor('hi')
            print('Test 2.1 StarSensor.initializeSensor() FAILED: Raised Exception when invalid filename passed')
        except:
            print('Test 2.1 StarSensor.initializeSensor() PASSED: Raised Exception when invalid filename passed')
        if (s.initializeSensor('data.txt') == 3):
            print('Test 2.2 StarSensor.initializeSensor() PASSED: Returned Correct value (number of stars) when passed file')
        else:
            print('Test 2.2 StarSensor.initializeSensor() FAILED: Returned InCorrect value (number of stars) when passed file')
    def test_3_StarSensor_configure(self):
        s = StarSensor(.1)
        e = Environment()
        if (s.configure(e)):
            print ('Test 3.1 StarSensor.configure() PASSED: returned true with valid Environment')
        else:
            print ('Test 3.1 StarSensor.configure() FAILED: returned false with valid Environment')
        try:
            s.configure('hi')
            print ('Test 3.2 StarSensor.configure() FAILED: Threw Error when passed invalid environment')
        except:
            print ('Test 3.2 StarSensor.configure() PASSED: Threw Error when passed invalid environment')
    def test_4_StarSensor_ServiceRequest(self):
        s = StarSensor(.1)
        if (s.serviceRequest() == None):
            print('Test 4.1 StarSensor.ServiceRequest(): PASSED: Returned None when null environment object')
        else:
            print('Test 4.1 StarSensor.ServiceRequest(): FAILED: Didnt return None when null environment object')
        e = Environment()
        e.setRotationalPeriod(40000000)
        s.configure(e)
        print(s.serviceRequest())
    def test_5_StarSensor_getSensorPosition(self):
        import math
        s = StarSensor(.1)
        e = Environment()
        s.configure(e)
        try:
            s.getSensorPosition()
            print('Test 5.1 StarSensor.getSensorPosition: FAILED: Threw Error when null rotationalTime')
        except:
            print('Test 5.1 StarSensor.getSensorPosition: PASSED: Threw Error when null rotationalTime')
        e = Environment()
        e.setRotationalPeriod(4000000)
        s.configure(e)
        list = s.getSensorPosition()
        if (list[0] == 2.0*math.pi and list[1] == 0):
            print('Test 5.2 StarSensor.getSensorPosition: PASSED: returned correct value when time == 0')
        else:
            print('Test 5.2 StarSensor.getSensorPosition: PASSED: returned correct value when time == 0')
        e.incrementTime(40)
        s.configure(e)
        list = s.getSensorPosition()
        if (list[0] >= -2*math.pi and list[1] >= -2*math.pi):
            print('Test 5.3 StarSensor.getSensorPosition: PASSED: returned correct value when running normally')
        else:
            print('Test 5.3 StarSensor.getSensorPosition: FAILED: returned incorrect value when running normally')
    def test_6_Environment_incrementTime(self):
        e = Environment()
        try:
            e.incrementTime('hi')
            print('Test 6.1 Environment.incrementTime(): FAILED: didnt throw error when incrementing by string')
        except:
            print('Test 6.1 Environment.incrementTime(): PASSED: threw error when incrementing by string')
        try:
            e.incrementTime(-1)
            print('Test 6.2 Environment.incrementTime(): FAILED: didnt throw error when incrementing by negative number')
        except:
            print('Test 6.2 Environment.incrementTime(): PASSED: threw error when incrementing by negative number')
        if (e.incrementTime(40) == 40):
            print('Test 6.3 Environment.incrementTime(): PASSED: worked Normally')
        else:
            print('Test 6.3 Environment.incrementTime(): FAILED: didnt work normally')
        if (e.getTime() == 40):
            print('Test 6.4 Environment.incrementTime()/getTime(): PASSED')
        else:
            print('Test 6.4 Environment.incrementTime()/getTime(): FAILED')
    def test_7_Environment_setRotationalPeriod(self):
        e = Environment()
        try:
            e.setRotationalPeriod('hi')
            print('Test 7.1 Environment.setRotationPeriod(): FAILED: didnt fail after passed string')
        except:
            print('Test 7.1 Environment.setRotationPeriod(): PASSED: threw exception when passed string')
        try:
            e.setRotationalPeriod(40)
            print('Test 7.2 Environment.setRotationPeriod(): FAILED: didnt fail after passing incorrect value')
        except:
            print('Test 7.2 Environment.setRotationPeriod(): PASSED: threw exception when passed incorrect value')
        if (e.setRotationalPeriod(4000000) == 4000000):
            print('Test 7.3 Environment.setRotationPeriod(): PASSED: returned correct value when passed good value')
        else:
            print('Test 7.3 Environment.setRotationPeriod(): FAILED: returned incorrect value when passed good value')
    def test_8_Environment_getRotationalPeriod(self):
        e = Environment()
        try:
            e.getRotationalPeriod()
            print('Test 8.1 Environment.setRotationPeriod(): FAILED: didnt throw exception for invalid rotationalperiod')
        except:
            print('Test 8.1 Environment.setRotationPeriod(): PASSED: threw exception for invalid rotationalperiod')
        e.setRotationalPeriod(4000000)
        if (e.getRotationalPeriod() == 4000000):
            print('Test 8.2 Environment.setRotationPeriod(): PASSED: worked correctly')
        else:
            print('Test 8.2 Environment.setRotationPeriod(): FAILED: worked incorrectly')
    def run_Tests(self):
        self.test_1_StarSensor_init()
        self.test_2_StarSensor_initializeSensor()
        self.test_3_StarSensor_configure()
        self.test_4_StarSensor_ServiceRequest()
        self.test_5_StarSensor_getSensorPosition()
        self.test_6_Environment_incrementTime()
        self.test_7_Environment_setRotationalPeriod()
        self.test_8_Environment_getRotationalPeriod()

t = Test()
t.run_Tests()
            
            

        
        
        
        