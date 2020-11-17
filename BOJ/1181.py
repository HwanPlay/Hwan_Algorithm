import sys
sys.stdin = open('input.txt', 'r')

arr_10 = [10, 13, 16, 19]
arr_20 = [20, 22, 24]
arr_30 = [30, 28, 27, 26]
arr_25 = [25, 30, 35, 40]

arr = [[0] + list(range(2, 41, 2)),
       arr_10,
       arr_20,
       arr_30,
       arr_25
       ]

ans = 0
pos = [[0, 0] for _ in range(4)]
check_final = [False] * 4
dices = list(map(int, input().split()))

def dfs(depth, result):
    if depth == 10:
        global ans
        if ans < result:
            ans = result
        return

    for idx in range(4):
        if check_final[idx]:
            continue
        x, y = pos[idx]
        dice = dices[depth]

        if x == 0:
            # if y == 0:
            y += dice
            if y == 5:
                x, y = 1, 0
            elif y == 10:
                x, y = 2, 0
            elif y == 15:
                x, y = 3, 0
            elif y == 20:
                x, y = 4, 3
            elif y > 20:
                check_final[idx] = True
        elif x == 1:
            if y+dice >= 8:
                check_final[idx] = True
            elif y + dice >= 4:
                x, y = 4, y + dice - 4
            else:
                y += dice
        elif x == 2:
            if y+dice >= 7:
                check_final[idx] = True
            elif y + dice >= 3:
                x, y = 4, y + dice - 3
            else:
                y += dice
        elif x == 3:
            if y+dice >= 8:
                check_final[idx] = True
            elif y + dice >= 4:
                x, y = 4, y + dice - 4
            else:
                y += dice
        elif x == 4:
            if y + dice >= 4:
                check_final[idx] = True
            else:
                y += dice
        isSame = False
        if not check_final[idx]:
            for j in range(4):
                if check_final[j]: continue
                if [x, y] == pos[j]:
                    isSame = True
        if isSame:
            continue
        pos_prev_x, pos_prev_y = pos[idx][0], pos[idx][1]

        if check_final[idx]:
            dfs(depth+1, result)
        else:
            pos[idx] = [x, y]
            dfs(depth+1, result + arr[x][y])
        if check_final[idx]:
            check_final[idx] = False
        pos[idx][0], pos[idx][1] = pos_prev_x, pos_prev_y
    return

dfs(0, 0)
print(ans)