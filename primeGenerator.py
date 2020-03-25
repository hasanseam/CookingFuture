testCase = int (input())

def primeGenatator(from_m,to_n):
    if from_m == 1:
        from_m +=1
        
    if from_m <10:
        for i in range(from_m, to_n+1):
         if i in [2,3,5,7]:
            print(i)
            continue
         if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            pass
         else:
            print(i)
    else:
        for i in range(from_m, to_n+1):
         if i%2==0 or i%3==0 or i%5==0 or i%7==0:
            pass
         else:
            print(i)

for i in range(testCase):
    from_m, to_n = map (int,input().split())
    primeGenatator(from_m,to_n)