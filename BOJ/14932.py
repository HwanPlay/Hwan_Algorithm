import sys
sys.stdin = open('input.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))


def abs(x):
    return x if x>0 else -x


l_pointer, r_pointer = 0, len(arr)-1
result = arr[l_pointer] + arr[r_pointer]
tmp = abs(arr[l_pointer] + arr[r_pointer])
while l_pointer+1 < r_pointer:

    if abs(arr[l_pointer]) > abs(arr[r_pointer]):
        l_pointer += 1
    elif abs(arr[l_pointer]) < abs(arr[r_pointer]):
        r_pointer -= 1
    else:
        tmp = 0
        break
    if tmp > abs(arr[l_pointer] + arr[r_pointer]):
        tmp = abs(arr[l_pointer] + arr[r_pointer])
        result = arr[l_pointer] + arr[r_pointer]
print(result)