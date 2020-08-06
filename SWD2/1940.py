T = int(input())

for t in range(1, T+1):
    N = int(input())
    
    command = [list(map(int, input().split())) for i in range(N)]
    
    s = 0
    d = 0
    
    for step in command:
        if step[0] == 1:
            s += step[1]
            d += s
        elif step[0] == 2:
            if s < step[1]:
                s = 0
            else:
                s -= step[1]
                d += s
        else:
            d += s
    
    print(f'#{t} {d}')