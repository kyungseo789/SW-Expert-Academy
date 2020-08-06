T = int(input())

for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    num = 0
    dx = [0, 1, 0, -1] #오른쪽, 아래, 왼쪽, 위
    dy = [1, 0, -1, 0]
    key = 0
    curX, curY = 0, -1

    while num < N * N:
        tmpX = curX + dx[key]
        tmpY = curY + dy[key]

        # 범위 초과시 방향 바꿔줌
        if tmpX < 0 or tmpY < 0 or tmpX >= N or tmpY >= N or arr[tmpX][tmpY] != 0:
            key += 1
            if key == 4:
                key = 0
        else:
            num += 1
            curX, curY = tmpX, tmpY
            arr[curX][curY] = num

    print('#{}'.format(t))
    for line in arr:
        print(' '.join(map(str, line)))