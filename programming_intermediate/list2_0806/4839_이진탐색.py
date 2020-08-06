import sys
sys.stdin = open('binary_search.txt', 'r')

T = int(input())
for t in range(1, T+1):
    page = list(map(int, input().split()))
    result = [0,0]
    for num in range(2):
        start = 1
        end = page[0]
        person = page[num+1]

        while start <= end:
            mid = (start + end)//2
            if person == mid:
                break
            elif person > mid:
                start = mid 
                result[num] += 1
            else:
                end = mid
                result[num]  += 1

    print('#{} {}'.format(t,'A' if result[0] < result[1] 
                          else (0 if result[0] == result[1] else 'B')))