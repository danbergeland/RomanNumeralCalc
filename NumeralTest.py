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

class NumeralXLetterCaseSetup(unittest.TestCase):
    def setUp(self):
        self.numeral = numeral.Numeral('X')

class NumeralXLetterisX(NumeralXLetterCaseSetup):
    def runTest(self):
        assert self.numeral.letter == 'X'
        
class NumeralXValueis10(NumeralXLetterCaseSetup):
    def runTest(self):
        assert self.numeral.value == 10
        
class NumeralLLetterCaseSetup(unittest.TestCase):
    def setUp(self):
        self.numeral = numeral.Numeral('L')
        
class NumeralLletterisL(NumeralLLetterCaseSetup):
    def runTest(self):
        assert self.numeral.letter == 'L'

class NumeralLvalueis50(NumeralLLetterCaseSetup):
    def runTest(self):
        assert self.numeral.value == 50