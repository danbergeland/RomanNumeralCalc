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
        
class TranslateCXCto190(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('CXC')==190
        
class IIVfailsDoubleSubtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('IIV')==-1
        
class CCMfailsDoubleSubtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('CCM')==-1
        
class VXfails5Subtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('VX')==-1
        
class LCfails5Subtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('LC')==-1
        
class DMfails5Subtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('DM')==-1
    
class VVfails5Repetition(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('VV')==-1

class LLfails5Reptition(CalculatorSetup):
    def runTest(self):
        assert  self.calc.roman2arabic('LL')==-1
        
class DDfails5Repitition(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('DD')==-1
        
class IIIIfailsMoreThan3Repitition(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('IIII')==-1
        
class CCCCfailsMoreThan3Repitition(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('CCCC')==-1
        
class ILfailsValidSubtraction(CalculatorSetup):
    def runTest(self):
        assert self.calc.roman2arabic('IL') == -1
        
class Translate2toII(CalculatorSetup):
    def runTest(self):
        assert self.calc.arabic2roman(2) == 'II'
        
class Translate1900toMCM(CalculatorSetup):
    def runTest(self):
        assert self.calc.arabic2roman(1900)=='MCM'
        
class Translate1800toMDCCC(CalculatorSetup):
    def runTest(self):
        assert self.calc.arabic2roman(1800)=='MDCCC'