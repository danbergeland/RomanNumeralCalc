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
        
class TranslateVIto6(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('VI')==6
        
class TranslateIVto4(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('IV')==4

class TranslateXLto40(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('XL')==40
        
class XXLfailsDoubleSubtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('XXL')==-1
    
class TranslateLXXto70(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('LXX')==70
        
class IIVfailsDoubleSubtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('IIV')==-1