T = int(input())
for t in range(1, T+1):
    N = int(input())
    ai = list(map(int, input().split())) #입력 A
    
    for i in range(0, len(ai)-1):
        min = i
        for j in range(i+1, len(ai)):
            if ai[min] > ai[j]:
                min = j
        ai[i], ai[min] = ai[min], ai[i]
    print('#{}'.format(t),end=' ')
    for n in ai:
        print(n ,end=' ')
    print()