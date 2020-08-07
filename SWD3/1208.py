for t in range(1, 11):
    N = int(input())
    ai = list(map(int,input().split()))
    cnt = 0
 
    while N+1:
 
        tmp_max = 0
        tmp_min = 100
        for i in ai:
            if tmp_max <= i:
                tmp_max = i
        for i in ai:   
            if tmp_min >= i:
                tmp_min = i
        ai[ai.index(tmp_max)] -= 1
        ai[ai.index(tmp_min)] += 1
         
        N -= 1
        # print(N, tmp_max, tmp_min)
    print('#{} {}'.format(t, tmp_max-tmp_min ))