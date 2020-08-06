n= int(input())
 
for test in range(1, n+1):
    m= int(input())
    number = list(map(int, input().split()))
    number.sort()
    counts = 0
    max_list = []
 
    for i in number:
        num_counts = number.count(i)
        if counts <= num_counts:
            counts = num_counts
            max_list.append(i)
    print(f'#{test} {max(max_list)}')