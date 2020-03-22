testCase = int(input())

for i in range(testCase):
    numberOfItems,numberOfItemsEachGroup = map(int, input().split())

    weightOfEachItems = [int(x) for x in input().split()]
    weightOfEachItems.sort()

    print(sum(weightOfEachItems[numberOfItemsEachGroup:])-sum(weightOfEachItems[:numberOfItemsEachGroup]))