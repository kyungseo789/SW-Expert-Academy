T = int(input())
for t in range(1, T+1):
    N = int(input())
    print('#{}'.format(t))
    answer = [0] * 8
    pay = [50000,10000,5000,1000,500,100,50,10]

    for i in range(len(pay)):
        answer[i] += N // pay[i]
        N %= pay[i]

    for j in answer:
        print(j, end=' ')
    print('')