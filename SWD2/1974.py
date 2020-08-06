T= int(input())
for t in range(1, T+1):
    N = [list(map(int,input().split())) for _ in range(9)]
    num_set = {1,2,3,4,5,6,7,8,9}
    answer = 0

    for i in range(9): #행
        if set(N[i]) == num_set: #가로 확인
            answer += 1

    for i in range(9): # 세로 확인
        tmp_list=[]
        for j in range(9):
            tmp_list.append(N[j][i])
        if set(tmp_list) == num_set:
            answer += 1

    for m in range(3):#첫 줄
        for n in range(3): #아래줄
            tmp_sq=[]
            for i in range(3): #가로
                for j in range(3): #세로
                    tmp_sq.append(N[i+3*m][j+3*n])    
            if set(tmp_sq) == num_set:    
                answer += 1

    print('#{} {}'.format(t, 1 if answer == 27 else 0))