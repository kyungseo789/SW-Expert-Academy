for t in range(1, 11):
    N= int(input())
    ai = list(map(int, input().split()))
    building = 0
    for i in range(2, len(ai)-2):
        if ai[i-2] < ai[i] and ai[i-1] < ai[i] and ai[i] > ai[i+1] and ai[i] > ai[i+2]:
            height_list= [ai[i]-ai[i-2], ai[i]-ai[i-1], ai[i]-ai[i+1], ai[i]- ai[i+2]]
            tmp_min = height_list[0]
            for j in height_list[1:]:
                if tmp_min > j:
                    tmp_min = j
            building += tmp_min
    print(f'#{t} {building}')