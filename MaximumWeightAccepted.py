testCase = int(input())

for i in range(testCase):
    numberOfItems,numberOfItemsEachGroup = map(int, input().split())

    weightOfEachItems = [int(x) for x in input().split()]
    weightOfEachItems.sort()
    minimumItemGotByChild = min(numberOfItemsEachGroup,numberOfItems-numberOfItemsEachGroup)
    print(sum(weightOfEachItems[minimumItemGotByChild:])-sum(weightOfEachItems[:minimumItemGotByChild]))