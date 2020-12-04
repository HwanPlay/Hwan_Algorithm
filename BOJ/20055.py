import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N, K = map(int, input().split())
belt = deque(list(map(int, input().split())))

# pos_machine = [False]*N
pos_machine = deque()
# Q 앞에 있는 machine가 belt에서 가장 뒤에 위치한다


def move_belt(Q):
    # 벨트 회전
    Q.appendleft(Q.pop())


def move_machine(belt, pos_machine):
    new_Q = deque()
    point = 0
    while pos_machine:
        x = pos_machine.popleft()
        x += 1
        if x == N-1:
            continue
        if not new_Q and belt[x+1]:
            x += 1
            belt[x] -= 1
            if not belt[x]:
                point += 1
        elif new_Q and new_Q[-1]>x+1 and belt[x+1]:
            x += 1
            belt[x] -= 1
            if not belt[x]:
                point += 1
        if x == N-1:
            continue
        new_Q.append(x)
    return new_Q, point


result, point = 1, 0
while True:
    move_belt(belt)
    if pos_machine:
        pos_machine, tmp = move_machine(belt, pos_machine)
        point += tmp
    if belt[0]:
        pos_machine.append(0)
        belt[0] -= 1
        if not belt[0]:
            point += 1

    if point >= K:
        break
    result += 1
print(result)