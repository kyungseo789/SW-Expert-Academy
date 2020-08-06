T= int(input())
for t in range(1, T+1):
    N = int(input())
    answer = 0

    for i in range(N):
        if i % 2: #index가 짝수
            answer += -(i+1)
        else:
            answer += i+1
    print('#{} {}'.format(t, answer))