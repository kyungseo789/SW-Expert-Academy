T= int(input())
for i in range(1, T+1):
    n= list(map(int,input().split()))
    result = 0
    days = [[1, 31],[2,28],[3,31],[4,30],[5,31],[6,30],
        [7,31],[8,31],[9,30],[10,31],[11,30],[12,31]]

    if n[0]==n[2]: #same month
        result = n[3] - n[1] +1

    else:
        result = days[n[0]-1][1] - n[1] +1 +n[3]
        for m in range(n[2]-n[0]-1):
            result += days[m+n[0]][1]
    print(f'#{i} {result}')