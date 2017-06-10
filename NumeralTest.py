import unittest
import numeral
    
class UnittestTestCase(unittest.TestCase):
    def runTest(self):
        assert True
    
class NumeralTestCaseSetup(unittest.TestCase):
    def setUp(self):
        self.numeral_ = numeral.Numeral('I')
        
class NumeralLetterIisI(NumeralTestCaseSetup):
    def runTest(self):
        assert self.numeral_.letter == 'I'
        
class NumeralValueIis1(NumeralTestCaseSetup):
    def runTest(self):
        assert self.numeral_.value == 1
