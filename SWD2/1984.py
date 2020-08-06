T= int(input())
for t in range(1, T+1):
    arr = list(map(int, input().split()))

    tmp_max = 0
    tmp_min = 10000
    tmp_sum = 0

    for i in arr: #최대,최소 구하기
        if i > tmp_max:
            tmp_max = i
        if i < tmp_min:
            tmp_min = i
    arr.pop(arr.index(tmp_max)) # 최대값 제거
    arr.pop(arr.index(tmp_min)) # 최소값 제거

    for i in arr: #평균 구하기
        tmp_sum += i
    print('#{} {}'.format(t, round(tmp_sum/len(arr))))