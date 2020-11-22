import sys
sys.stdin = open('input.txt', 'r')

result = 0
Stack = []
for _ in range(int(input())):
    n = int(input())
    if len(Stack) == 0:
        Stack.append(n)
    elif Stack[-1] > n:
        result += len(Stack)
        Stack.append(n)
    elif Stack[-1] <= n:
        while len(Stack) and Stack[-1] <= n:
            Stack.pop()
        result += len(Stack)
        Stack.append(n)
print(result)