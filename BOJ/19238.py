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
def isPassenger(x, y, passenger_arr):
    if passenger_arr[x][y]:
        return True
    return False

def changeTarget(x,y,d, nx,ny,nd):
    if nd < d:
        return nx, ny, nd
    elif nd == d:
        if nx < x:
            return nx, ny, nd
        elif nx==x:
            if ny < y:
                return nx,ny,nd
    return x,y,d

def find_passenger(pos_taxi, passenger_arr, map_arr):
    '''
    taxi 위치에서 승객까지 거리를 찾는다.
    타겟 승객의 위치, 거리를 반환,
    '''
    x, y = pos_taxi

    if passenger_arr[x][y]:  # 택시위치에 승객이 있을때
        return [x, y], 0
    distance_arr = [[0] * N for _ in range(N)]
    check_arr = [[False] * N for _ in range(N)]
    Q = deque([[x, y]])
    check_arr[x][y] = True
    px, py, pdistance = N, N, N**2
    while Q:
        [x, y] = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<N and 0<=ny<N) or check_arr[nx][ny] or \
                    map_arr[nx][ny]:
                continue

            if isPassenger(nx,ny, passenger_arr):
                px, py, pdistance = changeTarget(px, py, pdistance, nx, ny, distance_arr[x][y] + 1)

            check_arr[nx][ny] = True
            distance_arr[nx][ny] = distance_arr[x][y] + 1
            Q.append([nx, ny])

    return [px, py], pdistance

def go_to_dest(pos_taxi, dest_pos, arr):
    x, y = pos_taxi
    Q = deque([[x, y]])
    distance_arr = [[0]*N for _ in range(N)]
    check_arr = [[False]*N for _ in range(N)]
    check_arr[x][y] = True

    while Q:
        x, y = Q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if not (0<=nx<N and 0<=ny<N) or check_arr[nx][ny] or \
                arr[nx][ny]: continue
            distance_arr[nx][ny] = distance_arr[x][y] + 1
            check_arr[nx][ny] = True
            Q.append([nx,ny])
    tar_x, tar_y = dest_pos
    if check_arr[tar_x][tar_y]:
        return [tar_x, tar_y], distance_arr[tar_x][tar_y]
    else:
        return [N,N], N**2


Flag = True
while M:
    M -= 1
    pos_taxi, dis_passenger = find_passenger(pos_taxi, passenger_arr, arr)
    # x, y, 거리, # 목표 x, y
    if pos_taxi == [N, N] or dis_passenger == N**2:
        Flag = False
        break
    dest = passenger_arr[pos_taxi[0]][pos_taxi[1]]
    passenger_arr[pos_taxi[0]][pos_taxi[1]] = 0

    pos_taxi, dis_target = go_to_dest(pos_taxi, dest, arr)
    if pos_taxi == [N, N] or dis_target == N**2:
        Flag = False
        break
    if K - dis_passenger - dis_target >= 0:
        K += - dis_passenger + dis_target
    else:
        Flag = False
        break
if Flag:
    print(K)
else:
    print(-1)