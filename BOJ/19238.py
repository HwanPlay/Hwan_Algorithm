import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
pos_taxi = list(map(lambda x: int(x)-1, input().split()))
passenger_arr = [[0]*N for _ in range(N)]
for _ in range(M):
    px,py,dx,dy = map(lambda x: int(x)-1, input().split())
    passenger_arr[px][py] = [dx, dy]
# print(passenger_arr)

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
def find_passenger(pos_taxi, passenger_arr):
    sx, sy = pos_taxi
    if passenger_arr[sx][sy]:
        dest = passenger_arr[sx][sy]
        return [sx, sy, 0], dest

    distance_arr = [[-1]*N for _ in range(N)]
    Q = deque([[sx, sy]])
    distance_arr[sx][sy] = 0
    min_dis_passenger = [-1,-1,float('INF')]  # r,c,distance
    while Q:
        x, y = Q.popleft()
        if distance_arr[x][y] > min_dis_passenger[2]:
            break
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny] or distance_arr[nx][ny]>=0: continue
            # arr 1이면 벽, distance 양수이면 이미 방문한 곳
            if passenger_arr[nx][ny]:
                if distance_arr[x][y] + 1 < min_dis_passenger[2]:
                    min_dis_passenger = [nx,ny,distance_arr[x][y] + 1]
                elif distance_arr[x][y] + 1 == min_dis_passenger[2]:
                    if nx < min_dis_passenger[0]:
                        min_dis_passenger[:2] = nx, ny
                    elif nx == min_dis_passenger[0]:
                        if ny < min_dis_passenger[1]:
                            min_dis_passenger[1] = ny
            Q.append([nx, ny])
            distance_arr[nx][ny] = distance_arr[x][y] + 1
    dest = passenger_arr[min_dis_passenger[0]][min_dis_passenger[1]]
    passenger_arr[min_dis_passenger[0]][min_dis_passenger[1]] = 0
    if min_dis_passenger[:2] == [-1, -1]:
        return -1, -1
    return min_dis_passenger, dest

def go_to_dest(pos_taxi, dest_pos,):
    # print(, pos_taxi, dest_pos,)
    Q = deque([pos_taxi])
    dist_arr = [[-1]*N for _ in range(N)]
    dist_arr[pos_taxi[0]][pos_taxi[1]] = 0
    # print(Q)
    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if [nx, ny] == dest_pos:
                return dist_arr[x][y] + 1
            if not (0<=nx<N and 0<=ny<N): continue
            if arr[nx][ny] or dist_arr[nx][ny] != -1: continue
            dist_arr[nx][ny] = dist_arr[x][y] + 1
            Q.append([nx, ny])
    if dist_arr[dest_pos[0]][dest_pos[1]] == -1:
        return -1
    return dist_arr[dest_pos[0]][dest_pos[1]]


Fail = False
while M:
    M -= 1
    passenger_pos, dest_pos = find_passenger(pos_taxi, passenger_arr)
    # x, y, 거리, # 목표 x, y

    if passenger_pos == -1 or passenger_pos[2] > K:
        Fail = True
        break
    K -= passenger_pos[2]
    pos_taxi = passenger_pos[:2]
    dest = go_to_dest(pos_taxi, dest_pos)
    if dest == -1:
        Fail = True
        break
    pos_taxi = dest_pos
    if K >= dest:
        K += dest
    else:
        Fail = True
        break
    # print('dest', dest, Fail)

if Fail:
    print(-1)
else:
    print(K)