import unittest

class Tests(unittest.TestCase):
    
    def testCode(self):
        self.assertTrue(True, "hello")
        
if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))