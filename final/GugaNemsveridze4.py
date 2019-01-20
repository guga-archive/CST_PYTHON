from functools import reduce

class Diction:
    def __init__(self, myList = []):
        self.myList = myList
        print(self.myList)
        
    def getSumMinAndMax(self):
        print("SUM: " + str(reduce(lambda x, y: x + y, self.myList)) + "\n MIN: " + str(min(self.myList)) + "\n MAX: " + str(max(self.myList)))
    
l = [2, 4, 32, 16, 64]    
myDictionary = Diction(l)
myDictionary.getSumMinAndMax()
        