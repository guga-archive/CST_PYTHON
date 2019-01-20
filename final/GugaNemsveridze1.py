amountToPrint = int(input("Enter how many times you want to print: "))
result = ""
multiplier = 1
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = -1

for i in range(0, amountToPrint):
    if(i > multiplier * len(alphabet)-1):
        index = i - multiplier * len(alphabet)
        multiplier += 1
    else:
        index += 1
        
    result += alphabet[index]
    print(result + "\n")