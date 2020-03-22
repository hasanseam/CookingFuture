testCase = int(input())

def split(word): 
    return list(word)

def getResult(jewels,stones):
    result = 0
    for i in range(len(stones)):
        if stones[i] in jewels:
            result +=1
    
    return result


for i in range(testCase):
    jewels = input()
    stones = input()
    jewels = split(jewels)
    stones = split(stones)

    print(getResult(jewels,stones))