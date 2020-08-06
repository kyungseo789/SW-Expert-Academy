T = int(input())
for t in range(1, T + 1):
    N = int(input())
    print('#{}'.format(t))
    arr = [[0] * N for _ in range(N)]
    for i in range(N):
        arr[i][i] = 1
    for row in range(N):
        for col in range(row):
            if 0 <= row - 1:
                arr[row][col] += arr[row-1][col]
                if 0 <= col - 1:
                    arr[row][col] += arr[row-1][col-1]
        print(*arr[row][:row+1])