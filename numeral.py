

class Numeral:
    
    dictNumeralValues = {'I':1,'V':5, 'X':10,'L':50,'C':100,'M':1000}
    
    def __init__(self,numeralLetter):
        self.letter = numeralLetter
        self.value = 0
        try:
            self.getValue()
        except KeyError:
            self.letter = ''
            self.value = 0
        
        
    def getValue(self):
        self.value = self.dictNumeralValues[self.letter]
        

    