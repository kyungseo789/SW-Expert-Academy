import sys
sys.stdin = open('special_sort.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N= int(input())
    arr = list(map(int,input().split()))
    result_list = []
    
    while len(arr) > 0:
        tmp_max = 0
        tmp_min = 100
        for i in arr:
            if tmp_max < i :
                tmp_max = i
            if tmp_min > i:
                tmp_min = i
        result_list.append(arr.pop(arr.index(tmp_max)))
        result_list.append(arr.pop(arr.index(tmp_min)))
    
    print('#{}'.format(t), end=' ')
    for num in result_list[0:10]:
        print(num , end= ' ')
    print()