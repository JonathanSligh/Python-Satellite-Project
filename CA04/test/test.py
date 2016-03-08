'''
Created on November 30, 2015

@author: Jonathan
'''
from CA02.prod.Environment import Environment
from CA02.prod.StarSensor import StarSensor
from CA04.prod.SolarCollector import SolarCollector
class Test():
    def test_1_StarSensor_sunInViewTest(self):
        s = StarSensor(.00001)
        e = Environment()
        e.setRotationalPeriod(40000000)
        s.configure(e)
        if(s.isSunInView()):
            print("Test 1.1 StarSensor.isSunInView(): PASSED: worked correctly")
        else:
            print("Test 1.1 StarSensor.isSunInView(): FAILED: worked correctly")
    def test_2_SolarCollector_configureTest(self):
        e = Environment()
        e.setRotationalPeriod(40000000)
        sc = SolarCollector()
        try:
            sc.configure(e)
            print("Test 2.1 SolarCollector.configure(): PASSED: worked correctly")
        except(ValueError):
            print("Test 2.1 SolarCollector.configure(): FAILED: worked incorrectly")
        s = StarSensor(.1)
        try:
            sc.configure(s)
            print("Test 2.2 SolarCollector.configure(): FAILED: worked incorrectly")
        except(ValueError):
            print("Test 2.2 SolarCollector.configure(): PASSED: worked correctly")
    def test_3_SolarCollector_SunTest(self):
        s = StarSensor(.00001)
        e = Environment()
        e.setDegredation(50)
        e.setRotationalPeriod(40000000)
        s.configure(e)
        sc = SolarCollector()
        sc.configure(e)
        sc.starSensor = s
        if (sc.serviceRequest() == 16383.5):
            print("Test 3.1 SolarCollector.ServiceRequest(): PASSED: worked correctly")
        else:
            print("Test 3.1 SolarCollector.ServiceRequest(): FAILED: Not working correctly")
    def test_4_environment_degredation(self):
        e = Environment()
        try:
            e.setDegredation(50)
            print("Test 4.1 Environment.setDegredation(): PASSED: worked correctly")
        except(ValueError):
            print("Test 4.1 Environment.setDegredation(): FAILED: worked incorrectly")
        try:
            e.setDegredation(500)
            print("Test 4.2 Environment.setDegredation(): FAILED: worked incorrectly")
        except(ValueError):
            print("Test 4.2 Environment.setDegredation(): PASSED: worked correctly")
        try:
            e.setDegredation("hi")
            print("Test 4.3 Environment.setDegredation(): FAILED: worked incorrectly")
        except(ValueError):
            print("Test 4.3 Environment.setDegredation(): PASSED: worked correctly")
            
    def test_5_environment_startTime(self):
        e = Environment()
        try:
            e.setStartTime(50)
            print("Test 5.1 Environment.setDegredation(): PASSED: worked correctly")
        except(ValueError):
            print("Test 5.1 Environment.setDegredation(): FAILED: worked incorrectly")
        try:
            e.setStartTime(-1)
            print("Test 5.2 Environment.setDegredation(): FAILED: worked incorrectly")
        except(ValueError):
            print("Test 5.2 Environment.setDegredation(): PASSED: worked correctly")
        try:
            e.setStartTime("hi")
            print("Test 5.3 Environment.setDegredation(): FAILED: worked incorrectly")
        except(ValueError):
            print("Test 5.3 Environment.setDegredation(): PASSED: worked correctly")
    def run_Tests(self):
        self.test_1_StarSensor_sunInViewTest()
        self.test_2_SolarCollector_configureTest()
        self.test_3_SolarCollector_SunTest()
        self.test_4_environment_degredation()
        self.test_5_environment_startTime()
t = Test()
t.run_Tests()