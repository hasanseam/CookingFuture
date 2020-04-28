'''
https://www.codechef.com/problems/DIVIDING
Author: hasanseam
'''

number = int(input())

sumNumber = int((number*(number+1))/2)
stapmsOfAll = [int(x) for x in input().split()]

if sumNumber == sum(stapmsOfAll):
    print("YES")
else:
    print("NO")

    