N= int(input())
number = [str(num) for num in range(1, N+1)]
claps = ['3','6','9']

for num in number:
    if '3' in num or '6' in num or '9' in num:
        cnt = 0
        for clap in claps:
            cnt += num.count(clap)
        number[number.index(num)] = '-'*cnt

print(' '.join(number))