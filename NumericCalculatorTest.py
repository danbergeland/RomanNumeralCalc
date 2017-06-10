import unittest
import numericCalculator

class CalculatorSetup(unittest.TestCase):
    def setUp(self):
        self.calc = numericCalculator.Calculator()
        
class TranslateIto1(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('I')==1