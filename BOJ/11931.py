import sys
sys.stdin = open('input.txt', 'r')

tmp = set()
N = int(input())
for i in range(N):
    tmp.add(str(input()))
a = sorted(tmp, key=lambda x: (len(x), x))
print('\n'.join(a))