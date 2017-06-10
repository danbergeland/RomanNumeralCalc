import numeral

class Calculator:
    def __init__(self):
        self.arabic = 0
        self.roman = ''
        self.numerals = []
        
    def roman2arabic(self,romanLetters):
        self.roman = romanLetters
        self.parseRoman()
        self.evaluateNumerals()
        return self.arabic
    
    def arabic2roman(self,arabicNumber):
        self.arabic = arabicNumber
        self.roman = 'I'
        return self.roman
    
    def parseRoman(self):
        self.numerals = []
        for letter in self.roman:
            self.numerals.append(numeral.Numeral(letter))
            
    def evaluateNumerals(self):
        tempSum = 0
        for i in range(len(self.numerals)):
            numeral = self.numerals[i]
            if i==0:
                tempSum += numeral.value
            else:
                if(numeral.value<=self.numerals[i-1].value): 
                    tempSum += numeral.value
        self.arabic = tempSum
                