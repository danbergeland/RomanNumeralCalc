import numeral

class Calculator:
    def __init__(self):
        self.arabic = 0
        self.roman = ''
        
    def roman2arabic(self,romanLetters):
        self.roman = romanLetters
        self.arabic = 1
        return self.arabic