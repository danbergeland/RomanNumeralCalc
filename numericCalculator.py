import numeral

class Calculator:
    def __init__(self):
        self.arabic = 0
        self.roman = ''
        self.numerals = []
        
    def roman2arabic(self,romanLetters):
        self.roman = romanLetters
        self.parseRoman()
        if self.checkRomanNumeralGrammer():
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
                else:
                    tempSum = numeral.value - tempSum
        self.arabic = tempSum
        
    def checkRomanNumeralGrammer(self):
        checkPassed = True
        checkPassed = self.checkSingleSubtraction()
        if not checkPassed:
            self.arabic = -1
            self.roman = ''
            self.numerals = []
        return checkPassed
        
    def checkSingleSubtraction(self):
        iiIndex = self.roman.find('II')
        xxIndex = self.roman.find('XX')
        ccIndex = self.roman.find('CC')
        
        checkPassed = True
        if iiIndex>-1:
            checkPassed = self.checkNumeralsForHigherFollowerNumeral(iiIndex, numeral.Numeral('I'))
        if xxIndex>-1 and checkPassed:
            checkPassed = self.checkNumeralsForHigherFollowerNumeral(xxIndex, numeral.Numeral('X'))
        if ccIndex>-1 and checkPassed:
            checkPassed = self.checkNumeralsForHigherFollowerNumeral(startIndex, numeral.Numeral('C'))
            
        return checkPassed
                   
    def checkNumeralsForHigherFollowerNumeral(self,startIndex,numeral):
        for num in self.numerals[startIndex:]:
            if num.value > numeral.value:
                return False
        return True                 
            
                