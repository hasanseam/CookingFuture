a,b,c=map(int,input().split())
g=a+b+c
h=[]
for _ in range(g):
    h.append(int(input()))
h.sort()
k=[]
c=False
for i in range(g-1):
    if(h[i]==h[i+1]):
        c = True
    else:
        if(c!=0):
            k.append(h[i])
        c=0
print(len(k))        

for i in k:
    print (i)