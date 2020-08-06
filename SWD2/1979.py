T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    arr =[list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for i in arr: #가로방향
        cnt = 0
        for j in range(N):
            if i[j] == 0:
                if cnt == K : #앞 열에서 1이 K번 나온 경우
                    answer += 1
                cnt = 0
                continue
            cnt += 1
        if cnt == K:
            answer += 1

    for i in range(N): #세로방향
        cnt = 0
        for j in range(N):
            if arr[j][i] == 0:
                if cnt == K:
                    answer += 1
                cnt = 0
                continue
            cnt += 1
        if cnt == K:
            answer +=1
       
    print('#{} {}'.format(t, answer))