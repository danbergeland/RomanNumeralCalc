

class Numeral:
    
    dictNumeralValues = {'I':1,'V':5}
    
    def __init__(self,numeralLetter):
        self.letter = numeralLetter
        self.value = 0
        self.getValue()
        
    def getValue(self):
        self.value = self.dictNumeralValues[self.letter]
        

    