import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

dx = [0,0,-1,1]
dy = [1,-1,0,0]

N, M, G, R = map(int, input().split())
arr_map = []
result = 0
for _ in range(N):
    arr_map.append(list(map(int, input().split())))


def findPossible(arr):
    pos_arr = []
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                pos_arr.append([i, j])
    return pos_arr


arr_possible = findPossible(arr_map)
queue_rg = deque()


def bfs(Que):
    # print(Que)
    N_flower = 0
    Q = Que.copy()
    arr_color = [[0] * M for _ in range(N)]
    arr_sameTime = [[0] * M for _ in range(N)]
    # 1 = g, 2 = r, 3 = flower
    for q in Q:
        x, y, color, time = q
        arr_color[x][y] = color
        arr_sameTime[x][y] = time

    while Q:
        x, y, color, time = Q.popleft()
        if arr_color[x][y] == 3: continue

        for i in range(4):
            nx, ny = x + dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and arr_map[nx][ny] != 0:
                if arr_color[nx][ny] == 0:
                    arr_color[nx][ny] = color
                    arr_sameTime[nx][ny] = time + 1
                    Q.append([nx, ny, color, time+1])
                elif arr_color[nx][ny] == 3:
                    continue
                elif arr_color[nx][ny] != color and arr_sameTime[nx][ny] == time + 1:
                    arr_color[nx][ny] = 3
                    N_flower += 1

    global result
    if result < N_flower:
        result = N_flower


def choose_RG(arr, Q, depth, g, r):
    if len(arr)-depth < g+r:
        return
    if not g and not r:
        bfs(Q)
        return

    x, y = arr[depth]
    # 1은 g, 2는 r
    if g >= 1:  # g개수
        Q.append([x, y, 1, 1])
        choose_RG(arr, Q, depth+1, g-1, r)
        Q.pop()
    if r >= 1:
        Q.append([x, y, 2, 1])
        choose_RG(arr, Q, depth+1, g, r-1)
        Q.pop()
    choose_RG(arr, Q, depth+1, g, r)


choose_RG(arr_possible, queue_rg, 0, G, R)
print(result)