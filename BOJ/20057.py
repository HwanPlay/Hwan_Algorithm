import sys
sys.stdin = open('input.txt', 'r')

# L,D,R,U
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

send_sand = [
    [[0,0,2,0,0],
    [0,10,7,1,0],
    [5,-1,0,0,0],
    [0,10,7,1,0],
    [0,0,2,0,0]],
]
def rotate_send(arr):
    n = 5
    last = arr[-1]
    tmp_arr = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp_arr[n-1-j][i] = last[i][j]
    arr.append(tmp_arr)


for i in range(3):
    rotate_send(send_sand)
# print(send_sand)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

# print(arr)

x, y = N//2, N//2
check_arr = [[False]*N for _ in range(N)]
check_arr[x][y] = True
direction = 0


def make_dir(arr, x, y, direction):
    nx, ny = x+dx[(direction+1)%4], y+dy[(direction+1)%4]
    if not (0<=nx<N and 0<=ny<N) or not arr[nx][ny]:
        return (direction + 1)%4
    return direction


def move_tornado(arr, x, y, direction):
    x, y = x+dx[direction], y+dy[direction]
    rx,ry = -1, -1
    removed_sand = 0
    total_sand = 0
    sand = arr[x][y]
    for i in range(-2,3):
        for j in range(-2,3):
            nx, ny = x+i, y+j
            percent = send_sand[direction][i+2][j+2]
            if percent != -1:
                tmp_sand = (percent * sand) // 100
                total_sand += tmp_sand
                if 0<=nx<N and 0<=ny<N:
                    arr[nx][ny] += tmp_sand
                else:
                    removed_sand += tmp_sand
            else:
                rx,ry = nx, ny

    if 0<=nx<N and 0<=ny<N:
        arr[rx][ry] += sand - total_sand
    else:
        removed_sand += sand - total_sand

    # if 0<=x+dx[direction]<N and 0<=y+dy[direction]<N:
    #     arr[x+dx[direction]][y+dy[direction]] += sand - tmp
    # for i in arr:
    #     print(i)
    # print(tmp)

    return x,y,removed_sand

result = 0
for idx in range(N**2-1):
    if idx:
        direction = make_dir(check_arr, x, y, direction)

    x,y,tmp= move_tornado(arr, x, y, direction)
    check_arr[x][y] = True
    result += tmp

print(result)