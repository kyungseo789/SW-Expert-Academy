T = int(input())

for i in range(1, T+1):
    n = int(input())
    case = list(map(int, input().split()))
    answer = 0
    tem_max = case[-1]

    for j in case[::-1]:
        if tem_max >= j:
            answer += tem_max - j
        else:
            tem_max = j

    print(f'#{i} {answer}')