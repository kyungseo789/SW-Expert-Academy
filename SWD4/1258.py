T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    result = []
    for i in range(N):#가로방향 체크
        tmp_row = 0
        for j in range(N):
            if arr[i][j] != 0 and j != N-1: #0이 아닌 경우 행 수 체크
                tmp_row += 1
            elif arr[i][j] != 0 and j == N-1: #벽을 만나면
                tmp_row += 1
                result.append([j-tmp_row, tmp_row])
                tmp_row = 0
            else: #0을 만나면
                if tmp_row == 0:                    
                    continue                   
                else:
                    result.append([j-tmp_row, tmp_row]) #시작 idx, 행 수
                    tmp_row = 0
    
    answer = [] #행렬 찾기
    matrax_idx = [list(num) for num in set(tuple(item) for item in result)] 
    for i in matrax_idx:
        answer.append([result.count(i), i[1]])
    

    for i in range(len(answer)-1): #정렬하기
        min_idx = i
        for j in range(i+1, len(answer)):
            if answer[j][0]*answer[j][1]  < answer[min_idx][0]*answer[min_idx][1]:
                min_idx = j
            elif answer[j][0]*answer[j][1] == answer[min_idx][0]*answer[min_idx][1] and answer[j][0] < answer[min_idx][0]:
                min_idx = j
        answer[i], answer[min_idx] = answer[min_idx], answer[i]

    print('#{} {}'.format(t, len(answer)) , end= ' ')
    for i in answer:
        print(*i, end = ' ')
    print()