import unittest
import numericCalculator

class CalculatorSetup(unittest.TestCase):
    def setUp(self):
        self.calc = numericCalculator.Calculator()
        
class TranslateIto1(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('I')==1
        
class Translate1toI(CalculatorSetup):
    def runTest(self):
        assert self.calc.arabic2roman(1)=='I'
        
class TranslateIIto2(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('II')==2