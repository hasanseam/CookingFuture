testCase = int(input())

def isEven(NumberOfCoins):
     return True if NumberOfCoins%2 is 0 else False


for i in range(testCase):
    numberOfGames = int(input())
    for j in range(numberOfGames):
        initalStateOfCoin,NumberOfCoins,ResultStateOfCOin = map(int, input().split())
        result = int(NumberOfCoins/2)
        if(isEven(NumberOfCoins)):
            pass
        else:
            if(initalStateOfCoin==ResultStateOfCOin):
                pass
            else:
                result += 1
        print(result)