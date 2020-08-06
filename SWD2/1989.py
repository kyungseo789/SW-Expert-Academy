T= int(input())
for t in range(1, T+1):
    words = input()

    cnt = 0
    for i in range(len(words)//2):
        if words[i] == words[len(words)-1 - i]:
            cnt += 1

    print('#{} {}'.format(t, 1 if cnt == len(words)//2 else 0))