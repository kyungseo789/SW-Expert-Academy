for t in range(1, 11):
    T = int(input())
    N = [list(map(int, input().split())) for _ in range(100) ]
    max_sum = []
    answer = 0
    for x in N:
        sum = 0
        for num in x:
            sum += num
        max_sum.append(sum)
     
    for x in range(len(N)):
        sum = 0
        for y in range(len(N)):
            sum += N[y][x]
        max_sum.append(sum)
 
    sum = 0
    for x in range(len(N)):
        sum += N[x][x]
    max_sum.append(sum)
 
    sum = 0
    for x in range(len(N)):
        sum += N[x][len(N)-1 -x]
    max_sum.append(sum)
 
    for n in max_sum:
        if answer < n:
            answer = n
 
    print('#{} {}'.format(t,answer))