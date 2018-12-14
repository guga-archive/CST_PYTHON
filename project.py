def caesar():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    message = input("Enter your message: ")
    key = int(input("Enter your key: "))
    
    messageLength = len(message)
    
    cipheredText = ""
    
    for i in range(messageLength):
        character = message[i]
        location = alphabet.find(character)
        newLocation = (location + key) % 26
        cipheredText += alphabet[newLocation]
        
    print(cipheredText)
    
def caesarDecrypt():
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    
    message = input("Enter your message: ")
    key = int(input("Enter your key: "))
    
    messageLength = len(message)
    
    cipheredText = ""
    
    for i in range(messageLength):
        character = message[i]
        location = alphabet.find(character)
        newLocation = (location - key) % 26
        cipheredText += alphabet[newLocation]
        
    print(cipheredText)
    
    
caesar()
caesarDecrypt()
