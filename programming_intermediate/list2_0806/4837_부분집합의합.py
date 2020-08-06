import sys
sys.stdin = open('sum_of_subset.txt', 'r')

T = int(input())
for t in range(1, T+1):
    N,K = map(int, input().split())
    arr = [num for num in range(1, 13)]
  
    sub_total_set = []
    for i in range(1<<len(arr)): #전체 부분집합
        sub_set = []
        for j in range(len(arr)):
            if i & (1<<j):
                sub_set.append(arr[j])
        sub_total_set.append(sub_set)

    N_set_list = []
    for i in sub_total_set: #원하는 길이 부분집합
        if len(i) == N:
            N_set_list.append(i)

    answer = 0
    num_sum = 0
    N_num_list=[]
    for i in N_set_list:    #부분집합 원소의 합
        for j in i:
            num_sum += j
        N_num_list.append(num_sum)
    if K in N_num_list :
        answer += 1
    
    print('#{} {}'.format(t,answer))