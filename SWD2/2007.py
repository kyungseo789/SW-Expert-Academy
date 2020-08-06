T = int(input())
for t in range(1, T+1):
    N = input()
    result = []

    for i in range(10): #시작점
        for j in range(i+1, 10): #마디 안의 문자 수
            if N[i:i+j] == N[i+j+1: i+j+1+j]:
                result.append(j+1)
    print('#{} {}'.format(t,result[0]))#가장 첫 번째 수가 마디의 끝