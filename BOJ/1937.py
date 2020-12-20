import sys
sys.stdin = open('input.txt', 'r')

def solution():
    N = int(input())
    arr = [list(map(int, input().split())) for  _ in range(N)]
    check_arr = [[False]*N for _ in range(N)]
    distance_arr = [[0]*N for _ in range(N)]

    idx = 1
    for i in range(N):
        for j in range(N):
            if not check_arr[i][j]:
                idx += dfs(arr, check_arr, i, j, N)


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(arr, check_arr, x, y, N):
    tmp_color = arr[x][y]
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not (0<=nx<N and 0<=ny<N): continue
        if arr[nx][ny] > arr[x][y]:
            


    pass

solution()