import sys
t = int(input())

def binarySearch(arr,value,leftBound,rightBound):
    if(leftBound>rightBound or value<arr[leftBound] or value>arr[rightBound-1]):
        return -1
    
    middleBound = int((leftBound+rightBound)/2)
    if(arr[middleBound]==value):
        return middleBound
    else:
        if(arr[middleBound]<value):
            leftBound = middleBound
        else:
            rightBound = middleBound
    
    return binarySearch(arr,value,leftBound,rightBound)



def FindPositionAfterSorting(playlistLength,songsInPlaylist,previousPostionOfUncleJohnySong):
    lenthOfUncleJohnySong = songsInPlaylist[previousPostionOfUncleJohnySong-1]
    songsInPlaylist.sort()
    searchPosition = binarySearch(songsInPlaylist,lenthOfUncleJohnySong,0,playlistLength)
    return searchPosition


for i in range(t):
    playlistLength = int(input())
    songsInPlaylist=[int(x) for x in input().split()]
    previousPostionOfUncleJohnySong = int(input())
    newPositionOfUncleJohnySong = 1+FindPositionAfterSorting(playlistLength,songsInPlaylist,previousPostionOfUncleJohnySong) 
    print(newPositionOfUncleJohnySong)

