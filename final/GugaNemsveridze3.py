listOfFood = ["xachapuri", "xinkali", "mcvadi", "kababi", "salata"]

def shekvetis_gaketeba (shekveta):
    dictionary = {}
    for i in listOfFood:
        dictionary[i] = shekveta.count(i)
        
    result = ""
    for i, j in dictionary.items():
         result += str(i) + ":" + str(j) + " "
    print(result)
    
myOrder = input("Enter you order: ")
shekvetis_gaketeba(myOrder)