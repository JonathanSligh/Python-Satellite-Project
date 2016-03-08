'''
Created on Nov 1, 2015

@author: Jonathan
'''
class Test():
    def test_1_controller_initialize(self):
        from CA03.prod.Controller import Controller
        c = Controller()
        try:
            c.initialize("hahadf")
            print("Test 1.1 Controller.Initialize() FAILED: something bad/didnt raise valueerror")
        except ValueError:
            print("Test 1.1 Controller.Initialize() PASSED: raised valueerror when passed bad file name without .xml")
        if ((len(c.initialize("test.xml"))) == 3):
            print("Test 1.2 Controller.Initialize() PASSED: worked correctly")
        else:
            print("Test 1.2 Controller.Initialize() FAILED: worked incorrectly")
        try:
            c.initialize("test_invalid_device.xml")
            print("Test 1.3 Controller.Initialize() FAILED: Didn't catch invalid device")
        except ValueError:
            print("Test 1.3 Controller.Initialize() PASSED: Caught invalid device")
        try:
            c.initialize("test_invalid_num_params.xml")
            print("Test 1.4 Controller.Initialize() FAILED: Didn't catch invalid number of params")
        except ValueError:
            print("Test 1.4 Controller.Initialize() PASSED: Caught invalid number of params")
        try:
            c.initialize("test_invalid_params_name.xml")
            print("Test 1.5 Controller.Initialize() FAILED: Didn't catch invalid param name")
        except ValueError:
            print("Test 1.5 Controller.Initialize() PASSED: Caught invalid param name")
    def test_2_controller_run(self):
        from CA03.prod.Controller import Controller
        c = Controller()
        try:
            c.run(40)
            print("Test 2.1 Controller.Run() FAILED: Didnt catch when controller wasnt initialized")
        except ValueError:
            print("Test 2.1 Controller.Run() PASSED: Did catch when controller wasnt initialized")
        c.initialize("test.xml") 
        try:
            c.run("hi")
            print("Test 2.2 Controller.Run() FAILED: Didnt catch invalid param as string")
        except ValueError:
            print("Test 2.2 Controller.Run() PASSED: Caught invalid param as string")
        try:
            c.run(-2)
            print("Test 2.3 Controller.Run() FAILED: Didnt catch invalid negative param")
        except ValueError:
            print("Test 2.3 Controller.Run() PASSED: Caught invalid negative param")
        if (c.run(40) == 120):
            print("Test 2.4 Controller.Run() PASSED: WORKS CORRECTLY")
        else:
            print("Test 2.4 Controller.Run() PASSED: doesnt work lol")
    def test_3_monitor_initialize(self):
        from CA03.prod.Monitor import Monitor
        from CA02.prod.Environment import Environment
        m = Monitor()
        try:
            m.initialize("testbadfilename")
            print("Test 3.1 Monitor.Initialize() FAILED: something bad/didnt raise valueerror")
        except ValueError:
            print("Test 3.1 Monitor.Initialize() PASSED: raised valueerror when passed bad file name without .txt")
        if (not m.initialize("existingfile.txt")):
            print("Test 3.2 Monitor.Initialize() PASSED: returned false when passed an existing file")
        else:
            print("Test 3.2 Monitor.Initialize() FAILED: returned true when passed an existing file")
        if (m.initialize("notexistingfile.txt")):
            print("Test 3.3 Monitor.Initialize() PASSED: returned true when passed an non existing file")
        else:
            print("Test 3.3 Monitor.Initialize() FAILED: returned false when passed an non existing file")
    def test_4_monitor_configure(self):
        from CA03.prod.Monitor import Monitor
        from CA02.prod.Environment import Environment
        m = Monitor()
        e = Environment()
        fakeE = "hi"
        try:
            m.configure(fakeE)
            print("Test 4.1 Monitor.Configure() FAILED: didnt raise valueerror when passed bad environment")
        except ValueError:
            print("Test 4.1 Monitor.Configure() PASSED: raised valueerror when passed bad environment")
        if (m.configure(e)):
            print("Test 4.2 Monitor.Configure() PASSED: returned true when passed good environment")
        else:
            print("Test 4.2 Monitor.Configure() FAILED: didnt return true when passed good environment")
    def test_5_monitor_serviceRequest(self):
        from CA03.prod.Monitor import Monitor
        from CA02.prod.Environment import Environment
        badm = Monitor()
        m = Monitor()
        e = Environment()
        m.configure(e)
        m.initialize("test1.txt")
        try:
            badm.serviceRequest("hi", "hi", "hello")
            print("Test 5.1 Monitor.serviceRequest() FAILED: didnt raise valueerror when not initialized")
        except ValueError:
            print("Test 5.1 Monitor.serviceRequest() PASSED: did raise valueerror when not initialized")
        try:
            if (m.serviceRequest("hi", "hi", "hello") == 0):
                print("Test 5.2 Monitor.serviceRequest() PASSED: ran correctly!")
            else:
                print("Test 5.2 Monitor.serviceRequest() failed: didn't run correctly")
        except ValueError:
            print("Test 5.2 Monitor.serviceRequest() failed: raised valueerror when was supposed to run correctly")
    def test_6_device_configure(self):
        from CA03.prod.Device import Device
        from CA02.prod.Environment import Environment
        d = Device()
        e = Environment()
        fakeE = "hi"
        try:
            d.configure(fakeE)
            print("Test 6.1 Device.Configure() FAILED: didnt raise valueerror when passed bad environment")
        except ValueError:
            print("Test 6.1 Device.Configure() PASSED: raised valueerror when passed bad environment")
        if (d.configure(e)):
            print("Test 6.2 Device.Configure() PASSED: returned true when passed good environment")
        else:
            print("Test 6.2 Device.Configure() FAILED: didnt return true when passed good environment")
    def test_7_device_serviceRequest(self):
        from CA03.prod.Device import Device
        from CA02.prod.Environment import Environment
        d = Device()
        e = Environment()
        try:
            d.serviceRequest()
            print("Test 7.1 Device.ServiceRequest() FAILED: didnt throw valueerror when not initialized")
        except ValueError:
            print("Test 7.1 Device.ServiceRequest() PASSED: Threw valueerror when not initialized")
        d.configure(e)
        val = int(d.serviceRequest(), 16)
        if (val > 32767):
            val = (val - 32767)*-1
        if (val >= -32767 and val <= 32767):
            print("Test 7.2 Device.ServiceRequest() PASSED: returned correct value")
        else:
            print("Test 7.2 Device.ServiceRequest() FAILED: returned incorrect value")
                  
t = Test()
t.test_1_controller_initialize()
t.test_2_controller_run()
t.test_3_monitor_initialize()
t.test_4_monitor_configure()
t.test_5_monitor_serviceRequest()
t.test_6_device_configure()
t.test_7_device_serviceRequest()
            
    
        
        