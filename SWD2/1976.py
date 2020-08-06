T = int(input())
for t in range(1, T+1):
    ai = list(map(int, input().split()))
    min = (ai[1] +ai[3]) % 60
    if ((ai[1] +ai[3]) // 60) + ((ai[0] +ai[2]) % 12) == 0 :
        hour = 12
    else:
        hour = ((ai[1] +ai[3]) // 60) + ((ai[0] +ai[2]) % 12)

    print(f'#{t} {hour} {min}')