import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, Q = map(int, input().split())
# R, C = 2 ** N
RC = 2 ** N
cal_arr = [[[0]*RC for _ in range(RC)] for _ in range(2*Q)]
# 단계, R, C
arr = [list(map(int, input().split())) for _ in range(RC)]
# 0은 회전, 1은 얼음 제거
# arr에서 cal_arr로 처음에 회전된 값을 넣는다.
arr_Q = list(map(int, input().split()))


def move_ratate(prev, next, s_x, s_y, Q_step):
    for i in range(Q_step):
        for j in range(Q_step):
            next[s_x+j%Q_step][s_y-i+Q_step-1] = prev[s_x+i][s_y+j]


def rotate(prev_arr, next_arr, Q_level):
    Q_step = 2 ** Q_level
    length = len(prev_arr)
    for i in range(0, length, Q_step):
        for j in range(0, length, Q_step):
            move_ratate(prev_arr, next_arr, i, j, Q_step)


# -1 => 0 회전, 0 => 1 제거, 1=>2 회전,
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def remove_ice(prev, next, isFinal):
    n = len(prev)
    if isFinal:
        Q = deque()
    for i in range(n):
        for j in range(n):
            if not prev[i][j]: continue
            num_ice = 0
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if not (0<=nx<n and 0<=ny<n): continue
                if prev[nx][ny]>0: num_ice += 1
            if num_ice >= 3:  # and prev[i][j] > 0:
                next[i][j] = prev[i][j]
            else:
                next[i][j] = prev[i][j] - 1
            if isFinal:
                Q.append([i, j])
    if isFinal:
        return Q
    else:
        return 0


for idx in range(Q):
    if idx == 0:
        rotate(arr, cal_arr[0], arr_Q[idx])
    else:
        rotate(cal_arr[idx*2-1], cal_arr[idx*2], arr_Q[idx])

    # print('회전')
    # for i in cal_arr[idx*2]:
    #     print(i)
    # 제거
    # print('제거')
    isFinal = True if idx == Q-1 else False
    Que = remove_ice(cal_arr[idx*2], cal_arr[idx*2+1], isFinal)

    # for i in cal_arr[idx*2+1]:
    #     print(i)


def bfs(arr, Q, N):
    # print(arr)
    num_max = 0
    check_arr = [[False]*N for _ in range(N)]
    while Q:
        x, y = Q.popleft()
        if arr[x][y] and check_arr[x][y]: continue
        new_Q = deque()
        new_Q.append([x,y])
        tmp = 0
        while new_Q:
            tx, ty = new_Q.popleft()
            for i in range(4):
                nx, ny = tx+dx[i], ty+dy[i]
                if not (0<=nx<N and 0<=ny<N): continue
                if arr[nx][ny] and not check_arr[nx][ny]:
                    check_arr[nx][ny] = True
                    new_Q.append([nx, ny])
                    tmp += 1

        if tmp > num_max:
            num_max = tmp
    return num_max

def sum_arr(arr):
    result = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            result += arr[i][j]
    return result

print(sum_arr(cal_arr[-1]))
# print(sum(cal_arr[-1][:]))
print(bfs(cal_arr[-1], Que, RC))
