def finalList(biggerList,List1,List2):
    finalList = []

    for bl in biggerList:
        if bl in List1 or bl in List2:
            finalList.append(bl)
    
    for ls in List1:
        if ls in List2:
            if ls not in finalList:
                finalList.append(ls)
    
    finalList.sort()
    print(len(finalList))

    print ("\n".join(finalList))
        
        



N1,N2,N3 = map(int,input().split())
N1List = []
N2List = []
N3List = []

for i in range(N1):
    N1List.append(input())
    
for i in range(N2):
    N2List.append(input())
    
for i in range(N3):
    N3List.append(input())
    
if (N1>=N2 and N1>=N3):
    finalList(N1List,N2List,N3List)
elif(N2>=N1 and N2>=N3):
    finalList(N2List,N1List,N3List)
else:
    finalList(N3List,N1List,N2List)