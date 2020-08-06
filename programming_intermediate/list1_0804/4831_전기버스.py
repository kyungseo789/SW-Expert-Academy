import sys
sys.stdin = open('bus_input.txt', 'r')

T = int(input())
for t in range(1,T+1):
    K,N,M = map(int, input().split())
    bus_stop = list(map(int,input().split()))

    d = K
    cnt = 0
    tmp_d = 0

    for i in bus_stop:
        if i - d < K:
            for j in bus_stop:
                if d >= j:
                    tmp_d = j
            if d >= N:
                break
            d = tmp_d + K
            cnt += 1
        else:
            cnt = 0
            break 
    print('#{} {}'.format(t,cnt))