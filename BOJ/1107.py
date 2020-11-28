import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

N = int(input())
M = int(input())
if M:
    broken = list(map(int, input().split()))
else:
    broken = []

possible = []

check = [0] * 1000001
result = abs(N - 100)
Q = deque()
for i in range(10):
    if i not in broken:
        possible.append(i)
        Q.append(i)
        check[i] = 1

while Q:
    x = Q.popleft()
    if check[x] + abs(N-x) < result:
        result = check[x] + abs(N-x)

    for i in possible:
        if x*10 + i <= 1000000 and not check[x*10+i]:
            check[x*10+i] = check[x] + 1
            Q.append(x*10+i)

print(result)