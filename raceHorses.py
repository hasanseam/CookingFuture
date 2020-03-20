import sys
t = int(input())

def difference(number2,number1):
    return number2-number1
 
def evaluateMinimumDifference(n,arr):
    arr.sort()
    result = sys.maxsize
    for i in range(n-1):
        print(i)
        diff = difference(arr[i+1],arr[i])
        if diff<result:
            result = diff
    return result

for i in range(t):
    n = int(input())
    arr=[int(x) for x in input().split()]
    result = evaluateMinimumDifference(n,arr)
    #print(result)