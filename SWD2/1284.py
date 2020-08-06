case = int(input())
for i in range(1,case+1):
    p,q,r,s,w = map(int, input().split())
    companyA = 0
    companyB = 0

    companyA = p*w
    companyB = q if w <= r else q + (w-r)*s

    print(f'#{i} {min(companyA,companyB)}')