testCase = int(input())

def extraPageNeed(x,y):
    return x-y

def canChefBuy_A_NewNoteBook(notebooksPageAndPrice,newNotebookPageShouldBeAtleast,k_budget):
    for i in range(len(notebooksPageAndPrice)):
        if(notebooksPageAndPrice[i][0]>=newNotebookPageShouldBeAtleast and notebooksPageAndPrice[i][1]<=k_budget):
            return True
    return False
for i in range(testCase):
    x_pageNeedForPoetry,y_pageLeftForCurrentNotebook,k_budget,n_notebooksintheshop = map(int,input().split())
    notebooksPageAndPrice = []
    for j in range(n_notebooksintheshop):
        tempArr = [int(x) for x in input().split()]
        notebooksPageAndPrice.append(tempArr)
    newNotebookPageShouldBeAtleast = extraPageNeed(x_pageNeedForPoetry,y_pageLeftForCurrentNotebook)
    if(canChefBuy_A_NewNoteBook(notebooksPageAndPrice,newNotebookPageShouldBeAtleast,k_budget)):
        print("LuckyChef")
    else:
        print("UnluckyChef")