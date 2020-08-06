import sys
sys.stdin = open('number_card.txt', 'r')

T = int(input())
for t in range(1,T+1):
    N = int(input())
    ai = input()
    cnt_list=[]
    max_list=[]
    max_cnt_num = ai[0]

    for j in set(list(ai)):
        if ai.count(j) >= ai.count(max_cnt_num) and int(j) > int(max_cnt_num):
            max_cnt_num = j

    print('#{} {} {}'.format(t,max_cnt_num,ai.count(max_cnt_num)))