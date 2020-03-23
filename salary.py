'''
Problem Statement: https://www.codechef.com/problems/SALARY
Author: hasanseam
'''
testCase = int(input())

def increaseSalary(wagesOfworkers,excepPosition):
    for i in range(len(wagesOfworkers)):
        if i==excepPosition:
            continue
        wagesOfworkers[i]+=1
    
    return wagesOfworkers

def getMaxPosition(wagesOfworkers,maxwage):
    for i in range(len(wagesOfworkers)):
        if maxwage == wagesOfworkers[i]:
            return i

for i in range(testCase):
    numberOfWorkers = int(input())
    wagesOfworkers = [int(x) for x in input().split()]
    
    maxWage = max(wagesOfworkers)
    result = 0
    count = 0
    while maxWage!=sum(wagesOfworkers)/len(wagesOfworkers):
        result +=1
        maxPosition = getMaxPosition(wagesOfworkers,maxWage)
        wagesOfworkers = increaseSalary(wagesOfworkers,maxPosition)
        maxWage = max(wagesOfworkers)
        print(wagesOfworkers)
    
    print(result)