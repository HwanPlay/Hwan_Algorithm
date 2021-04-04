import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

n_node_children = [[] for _ in range(N+1)]                   # 자식 노드 저장
b_is_visited = [False] * (N+1)

ans = []                            # 자식 노드의 개수

for i in range(M):
    A, B = map(int, input().split())
    n_node_children[B].append(A)

max_val = 0

for i in range(1, N+1):
    if not n_node_children[i]:
        continue

    Q = deque([i])
    b_is_visited[i] = True
    tmp = 1
    while Q:
        parent_node = Q.popleft()
        for child_node in n_node_children[parent_node]:
            if child_node and not b_is_visited[child_node]:
                b_is_visited[child_node] = True
                Q.append(child_node)
                tmp += 1

    b_is_visited = [False] * (N + 1)

    if tmp > max_val:
        ans = [i]
        max_val = tmp
    elif tmp == max_val:
        ans.append(i)

str_result = ''

for i in ans:
    str_result += str(i) + ' '
print(str_result)