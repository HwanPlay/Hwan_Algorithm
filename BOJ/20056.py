import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, M, K = map(int, input().split())
# class qw():
#     def __init__(self):



# arr = [[[] for _ in range(N)] for _ in range(N)]
# K, N, N
# print(arr)
Que = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    Que.append([r, c, m, s, d])

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]


def move(Q):
    new_Q = deque()
    pos_Q = deque()
    new_arr = [[[] for _ in range(N)] for _ in range(N)]

    # print(Q)
    while Q:
        r, c, m, s, d = Q.popleft()
        nr = (r + dx[d]*s + N)%N
        nc = (c + dy[d]*s + N)%N
        if not len(new_arr[nr][nc]):
            pos_Q.append([nr,nc])
        new_arr[nr][nc].append([m,s,d])
    # print(pos_Q)
    while pos_Q:
        x, y = pos_Q.popleft()
        msd = new_arr[x][y]
        # print(msd)
        if len(msd) >= 2:
            weight, speed, direction = 0, 0, -1
            for ele_msd in msd:
                if direction == -1:
                    direction = ele_msd[2]&1 # 0 짝, 1 홀수
                elif direction == 1: # 홀수
                    if ele_msd[2]&1 == 0: # 짝수
                        direction = -2  # 1,3,5,7
                    elif ele_msd[2]&1 == 1: # 홀수
                        direction = 1
                elif direction == 0: # 짝수
                    if ele_msd[2]&1 == 0: # 짝수
                        direction = 0  # 1,3,5,7
                    elif ele_msd[2]&1 == 1: # 홀수
                        direction = -2
                weight += ele_msd[0]
                speed += ele_msd[1]
            weight //= 5
            if weight  == 0: continue
            speed //= len(msd)
            if direction == -2:
                for i in [1,3,5,7]:
                    new_Q.append([x,y,weight,speed,i])
            else:
                for i in [0,2,4,6]:
                    new_Q.append([x,y,weight,speed,i])
        else:
            new_Q.append([x, y, *msd[0]])
    # print('newQ', new_Q)
    return new_Q


for step in range(K):
    Que = move(Que)
result = 0
for _,_,w,_,_ in Que:
    result += w

print(result)