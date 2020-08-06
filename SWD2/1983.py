import sys
sys.stdin = open('swd2_1983.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N, P = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    grade = ['A+', 'A0', 'A-','B+','B0','B-','C+','C0','C-','D0']
    result = []

    for k in range(N): #[학생 순번, 총점]
        result.append([ k+1, arr[k][0]*0.35 + arr[k][1]*0.45 + arr[k][2]*0.2])
    
    for i in range(N-1): #높은 순으로 정렬
        max_idx = i
        for j in range(i+1, N):
            if result[j][1] > result[max_idx][1]:
                max_idx = j
        result[i] , result[max_idx] = result[max_idx], result[i]

    step = 0
    for i in grade: #높은 순으로 성적 추가
        sub_step = 0
        for j in range(N//10):
            result[j+step].append(i)
            sub_step += 1
        step += sub_step
    
    for i in range(N):
        if result[i][0] == P:
            print('#{} {}'.format(t, result[i][2]))