import numeral

class Calculator:
    def __init__(self):
        self.arabic = 0
        self.roman = ''
        
    def roman2arabic(self,romanLetters):
        self.roman = romanLetters
        self.arabic = 1
        return self.arabic
    
    def arabic2roman(self,arabicNumber):
        self.arabic = arabicNumber
        self.roman = 'I'
        return self.roman