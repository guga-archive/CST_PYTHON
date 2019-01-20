import random

randomNumber = random.randint(0, 5)
if randomNumber == 1:
    words = []
    for i in range (1, 5):
        word = input ("Enter word #: " + str(i) + " ")
        words.append(word)
    
    for a in words:
        print(a[1])
        
elif randomNumber == 2:
    numbers = []
    for i in range (1, 9):
        number = input("Enter number #:" + str(i) + " ")
        numbers.append(number)
        
    for i in range(len(numbers)):
        if i % 2 == 0:
            numbers[i] = ''
            
    while '' in numbers:
        numbers.remove('')
    print(numbers)
    
elif randomNumber == 4:
    dictionary = {}
    for i in range(1, 6):
        key = input("Enter word " + str(i) + ": ")
        dictionary[key] = int(input("Enter number " + str(i) + ": "))
    print (dictionary)
    
    for i, j in d.items():
        myTuple = (i, j)
        print (myTuple)
        
elif randomNumber == 5:
    text = input("Enter text: ")
    words = text.split()
    print(words)
        
        
        
        