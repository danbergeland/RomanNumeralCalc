

class Numeral:
    
    dictNumeralValues = {'I':1,'IV':4,'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50, 'XC':90,'C':100, 'CD':400, 'D':500,'CM':900,'M':1000}
    listValidSubtractions = ['IV','IX','XL','XC','CD','CM']
    
    def __init__(self,numeralLetter):
        self.letter = numeralLetter
        self.value = 0
        try:
            self.getValue()
        except KeyError:
            self.letter = ''
            self.value = 0
            
    def __lt__(self, other):
        return self.value < other.value
    
    def __str__(self):
        return self.letter
        
        
    def getValue(self):
        self.value = self.dictNumeralValues[self.letter]
        

    