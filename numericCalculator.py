import numeral

class Calculator:
    def __init__(self):
        self.arabic = 0
        self.roman = ''
        self.numerals = []
        
    def roman2arabic(self,romanLetters):
        self.roman = romanLetters
        if self.checkRomanNumeralGrammer():        
            self.parseRoman()
            self.evaluateNumerals()
        return self.arabic
    
    def arabic2roman(self,arabicNumber):
        self.arabic = arabicNumber
        if(self.arabic > 0):
            self.generateRomanNumerals()
        return self.roman
    
    
    '''
    
    ROMAN 2 ARABIC FUNCTIONS
    
    '''    
    
    def parseRoman(self):
        self.numerals = []
        #check for subtractions by creating with pairs at each index
        for numPairs in numeral.Numeral.listValidSubtractions:
            splitLetters = self.roman.split(sep=numPairs, maxsplit=1)
            if len(splitLetters)> 1:
                self.numerals.append(numeral.Numeral(numPairs))
            self.roman = ''.join(splitLetters)
        #Now that subs are removed, add the remaining numerals        
        for l in self.roman:
            self.numerals.append(numeral.Numeral(l))
        #sort them, so they should appear in C, XC, X... descending order
        self.numerals.sort(reverse=True)
            
    def evaluateNumerals(self):
        tempSum = 0
        for num in self.numerals:
            tempSum += num.value
        self.arabic = tempSum
        
    def checkRomanNumeralGrammer(self):
        checkPassed = True
        checkPassed = self.checkSingleSubtraction()
        if checkPassed:
            checkPassed = self.checkFiveBasedSubtraction()
        if checkPassed:
            checkPassed = self.checkMoreThan3Repetition()
        if checkPassed:
            checkPassed = self.checkValidSubtraction()
        
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
            checkPassed = self.checkFollowingNumeralsLessThanEqual(iiIndex, numeral.Numeral('I'))
        if xxIndex>-1 and checkPassed:
            checkPassed = self.checkFollowingNumeralsLessThanEqual(xxIndex, numeral.Numeral('X'))
        if ccIndex>-1 and checkPassed:
            checkPassed = self.checkFollowingNumeralsLessThanEqual(ccIndex, numeral.Numeral('C')) 
        return checkPassed
          
    def checkFiveBasedSubtraction(self):
        checkPassed = True
        fiveBasedNumbers = ['V','L','D']
        for num in fiveBasedNumbers:
            index = self.roman.find(num)
            if index > -1:
                checkPassed = self.checkFollowingNumeralsLessThan(index, numeral.Numeral(num))
        return checkPassed
    
    def checkMoreThan3Repetition(self):
        forbiddenStrings = ['IIII','XXXX','CCCC','MMMM']
        for str in forbiddenStrings:
            if self.roman.find(str)>-1:
                return False
        return True
    
    def checkValidSubtraction(self):
        dictValidFollowers = {'I':['I','V','X'],'X':['I','V','X','L','C'],'C':['I','V','X','L','C','D','M']}
        checkPassed = True
        for num in dictValidFollowers:
            index = self.roman.find(num)
            if index > -1 and index+1 < len(self.roman):
                checkPassed = self.roman[index+1] in dictValidFollowers[num]
        return checkPassed

                
    def checkFollowingNumeralsLessThanEqual(self,startIndex,numer):
        for letter in self.roman[startIndex:]:
            num = numeral.Numeral(letter)
            if num.value > numer.value:
                return False
        return True                
    
    def checkFollowingNumeralsLessThan(self,startIndex,numer):
        for letter in self.roman[startIndex+1:]:
            num = numeral.Numeral(letter)
            if num.value >= numer.value:
                return False
        return True
    '''
    
    ARABIC 2 ROMAN Functions
    
    '''
    def generateRomanNumerals(self):
        self.roman = ''
        self.numerals = []
        remainingNumber = self.arabic
        
        listDescendingNumerals = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        #Go get the largest numeral/subtraction pair, and subtract it from the temp
        while remainingNumber > 0:
            for num in listDescendingNumerals:
                if remainingNumber >= numeral.Numeral.dictNumeralValues[num]:
                    self.numerals.append(numeral.Numeral(num))
                    remainingNumber -= numeral.Numeral.dictNumeralValues[num]
                    break

        for num in self.numerals:
            self.roman += num.letter