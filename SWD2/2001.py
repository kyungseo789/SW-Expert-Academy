T= int(input())
for t in range(1, T +1):
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = 0
    
    for n in range(N-M+1):
        for m in range(N-M+1):
            tmp_sum = 0
            for i in range(M):
                for j in range(M):
                    tmp_sum += arr[n+i][m+j]
            if result < tmp_sum:
                result = tmp_sum
    print('#{} {}'.format(t, result))