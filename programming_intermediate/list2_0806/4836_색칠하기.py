import sys
sys.stdin = open('color.txt', 'r')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    ai = [list(map(int, input().split())) for _ in range(N)]
    red = []
    blue = []
    for i in range(N):  # 네모 갯수
        startX = ai[i][0]
        startY = ai[i][1]
        for x in range(ai[i][2] - ai[i][0] + 1):
            for y in range(ai[i][3] - ai[i][1] + 1):  # 가로만
                if ai[i][4] == 1:  # red
                    red.append([startX + x, startY + y])
                else:  # blue
                    blue.append([startX + x, startY + y])

    color_blue = len(blue)
    for purple in red:
        if purple in blue:
            blue.remove(purple)

    print('#{} {}'.format(t, color_blue - len(blue)))