import sys
sys.stdin = open('min_max.txt', 'r')

T = int(input())

for t in range(1,T+1):
    N= int(input())
    ai = list(map(int, input().split()))
    tmp_max = ai[0]
    tmp_min = ai[0]

    for num in ai:
        if tmp_max < num:
            tmp_max = num
        if tmp_min > num:
            tmp_min = num

    print('#{} {}'.format(t, tmp_max - tmp_min))