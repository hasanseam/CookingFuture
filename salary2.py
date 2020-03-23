'''
Problem Statement: https://www.codechef.com/problems/SALARY
Author: hasanseam
'''
testCase = int(input())

for i in range(testCase):
    numberOfWorkers = int(input())
    wagesOfWorkers = [int(x) for x in input().split()]

    minimumSalary = min(wagesOfWorkers)

    sumOfTheSalary = sum(wagesOfWorkers)

    print(sumOfTheSalary - numberOfWorkers*minimumSalary)
    
    
