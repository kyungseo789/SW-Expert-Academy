import sys
sys.stdin = open('part_of_sum.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N,M = map(int, input().split())
    ai = list(map(int, input().split()))
    tmp_min = 1e+10
    tmp_max = 0

    for i in range(0, N-M+1):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += ai[i+j]
        if tmp_min > tmp_sum:
            tmp_min = tmp_sum
        if tmp_max < tmp_sum:
            tmp_max = tmp_sum

    print('#{} {}'.format(t,tmp_max - tmp_min ))