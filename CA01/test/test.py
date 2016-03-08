'''
Created on Sep 1, 2015

@author: Jonathan Sligh
'''
from CA01.prod import StarCatalog
class Test():
    s = None
    def test_1_catalog(self):
        s = StarCatalog()
        try: s.loadCatalog("ssss")
        except: print("Test 1.1 Passed: invalid file")
        try: s.loadCatalog("star_file_dupTest.txt")
        except: print("Test 1.2 Passed: Duplicate Star Detected")
        try:s.loadCatalog("star_file_test.txt")
        except: print("Test 1.3 FAILED!!!!!!")
        print ("Test 1.3 Passed: Normal functioning.")
    def test_2_emptyCatalog(self):
        s = StarCatalog()
        s.loadCatalog("star_file.txt")
        s.emptyCatalog()
        if (len(s.starList) == 0):
            print ("Test 2.0 Passed: Empty Catalog Worked")
    def test_3_getStarCount(self):
        s = StarCatalog()
        s.loadCatalog("star_file_test.txt")
        try: s.getStarCount("hi", 1)
        except: print ("Test 3.1 Passed: Invalid LowerMagnitude")
        try: s.getStarCount(1, "lol")
        except: print ("Test 3.2 Passed: Invalid UpperMagnitude")
        try: s.getStarCount(30, 1)
        except: print ("Test 3.3 Passed: Lower Magnitude > Upper Magnitude")
        if (s.getStarCount() == 3):
            print ("Test 3.4 Passed: No params, returned all stars")
        try: count = s.getStarCount(0, 5)
        except: print("Test 3.5 failed!!!!")
        if (count == 3):
            print ("Test 3.5 passed: Normal getStarCount")
        else:
           print("Test 3.5 failed!!!!") 
    def test_4_getMagnitude(self):
        s = StarCatalog()
        s.loadCatalog("star_file_test.txt")
        try: s.getMagnitude(50, 0, 3.14)
        except: print("Test 4.1 Passed: Invalid RightAscension")
        try: s.getMagnitude(0, 50, 3.14)
        except: print("Test 4.2 Passed: Invalid Centerpoint")
        try: s.getMagnitude(0, 0, 50)
        except: print("Test 4.3 Passed: Invalid fieldOfView")
        try: mag = s.getMagnitude(0, 3, 6)
        except: print("Test 4.4 FAILED!!!!")
        if (mag == 1):
            print("Test 4.4 Passed: Get Magnitude normal work")
        else:
            print("Test 4.4 FAILED!!!!")
    def test_5_loadCatalog(self):
        s = StarCatalog()
        s.loadCatalog("star_file_test.txt")
        if (s.getStarCount(None, None) == 2):
            print"Test 5.1 passed: loaded 2 stars"
    def run_tests(self):
        self.test_1_catalog()
        self.test_2_emptyCatalog()
        self.test_3_getStarCount()
        self.test_4_getMagnitude()
        self.test_5_loadCatalog()
t = Test()
t.run_tests()
