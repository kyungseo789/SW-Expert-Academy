a = int(input())
for x in range(1, a+1):
    n = int(input())
    cnt = 0
    
    zero_to_nine = [str(i) for i in range(10)]
    while zero_to_nine:
        cnt += 1
        num = n * cnt
        num = str(num)

        for c in num:
            if c in zero_to_nine:
                zero_to_nine.remove(c)

    print(f'#{x} {num}')