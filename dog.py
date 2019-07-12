#Anjali Kumari
#class HW
#11/20/2017
class Dog:
    species = 'Canis familiaris'
    def __init__(self, Name, Breed):
        self.name = Name
        self.breed = Breed
        self.tricks = []
    def teach(self, Tricks):
        k = self.name + ' knows ' + str(Tricks)
        self.tricks.append(k)
        print(k)
    def knows(self, Trick):
        for words in self.tricks:
            if str(Trick) in words:
                print('Yes, ' + self.name + ' knows ' + str(Trick))
                return True
            else:
                print('No, ' + self.name + ' does not know ' + str(Trick))
                return False
        
        
        
        
            
            
        
    

        
    
    
        
        
        
