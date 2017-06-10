import unittest
import numeral
    
class UnittestTestCase(unittest.TestCase):
    def runTest(self):
        assert True
    
class NumeralITestCaseSetup(unittest.TestCase):
    def setUp(self):
        self.numeral_ = numeral.Numeral('I')
        
class NumeralILetterisI(NumeralITestCaseSetup):
    def runTest(self):
        assert self.numeral_.letter == 'I'
        
class NumeralIValueis1(NumeralITestCaseSetup):
    def runTest(self):
        assert self.numeral_.value == 1

class NumeralVLetterCaseSetup(unittest.TestCase):
    def setUp(self):
        self.numeral = numeral.Numeral('V')
        
class NumeralVLetterisV(NumeralVLetterCaseSetup):
    def runTest(self):
        assert self.numeral.letter == 'V'
        
class NumeralVValueis5(NumeralVLetterCaseSetup):
    def runTest(self):
        assert self.numeral.value == 5