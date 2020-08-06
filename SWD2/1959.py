T = int(input())
for i in range(1, T+1):
    N, M = input().split()
    result=[]
    max_list = []
    for j in range(2):
        n=list(map(int, input().split()))
        result.append(n)
    if len(result[0]) < len(result[1]):
        for m in range((len(result[1]) - len(result[0]))+1):
            tmp_max = 0
            for n in range(len(result[0])):
                tmp_max += result[0][n] * result[1][n+m]
            max_list.append(tmp_max)
    else:
         for m in range((len(result[0]) - len(result[1]))+1):
            tmp_max = 0
            for n in range(len(result[1])):
                tmp_max += result[1][n] * result[0][n+m]
            max_list.append(tmp_max)       

    print(f'#{i} {max(max_list)}')