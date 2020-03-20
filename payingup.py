testCase = int(input())

def getResult(bankNotesValue,amountOfMoney):
    for i in range(len(bankNotesValue)):
        if(amountOfMoney==0):
            break
        if(bankNotesValue[i]<=amountOfMoney):
            amountOfMoney -= bankNotesValue[i]
    
    return amountOfMoney

for i in range(testCase):
    numberOfNotes,amountOfMoney = map(int, input().split())
    bankNotesValue = []
    for j in range(numberOfNotes):
        k = int(input())
        bankNotesValue.append(k)
    bankNotesValue.sort()
    bankNotesValue.reverse()
    result = getResult(bankNotesValue,amountOfMoney)
    print("Yes") if result==0 else print("No")
