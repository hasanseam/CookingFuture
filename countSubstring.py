'''
Problem Statement: https://www.codechef.com/problems/CSUB
Author: hasanseam
'''
testCase = int(input())

for i in range(testCase):
    character = int(input())
    mainString = input()
    result = mainString.count("1")
    print(int((result*(result+1))/2))