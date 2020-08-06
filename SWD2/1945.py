T = int(input())
for i in range(1, T+1):
    n= int(input())
    a,b,c,d,e= 0,0,0,0,0
    
    while n % 2 == 0:
        n = n//2
        a +=1

    while n % 3 == 0:
        n = n//3
        b +=1
        
    while n % 5 == 0:
        n = n//5
        c +=1
        
    while n % 7 == 0:
        n = n//7
        d +=1
        
    while n % 11 == 0:
        n = n//11
        e +=1

    print(f'#{i} {a} {b} {c} {d} {e}')