import sys
sys.stdin = open('input.txt', 'r')

arr = input()
stack = []

brackets = {'(':0, ')':1, '[':2, ']':3}

def checkBracket(bracket):
    if bracket == '(': return 0
    elif bracket == ')': return 1
    elif bracket == '[': return 2
    return 3

def isNumber(arr, bracket):
    idx = len(arr)-1
    result = 0
    while arr[idx] not in ['(', ')', '[', ']'] and 0 <= arr[idx] <= 9:
        result += arr[idx]
        arr.pop()
        idx -= 1
    if arr[idx] == bracket:
        return result
    return 0, 0


def calStack(arr, num_bracket):
    # 닫는 괄호 1 ), 3 ]
    idx = len(arr)-1
    sum_inner = 0
    if num_bracket == 1:  # 1, )
        if arr[-1] == '(':
            arr.pop()
            arr.append(2)
            return 1
        elif arr[-1] in [']', ')']: return 0
        else:
            tmp = isNumber(arr, '(')
            if tmp:
                sum_inner += tmp * 2
            else:
                return 0
    else:  # 3, ]
        if arr[-1] == '[':
            arr.pop()
            arr.append(3)
            return 1
        elif arr[-1] in [']', ')']: return 0
        else:
            tmp, th = isNumber(arr, '[')
            if tmp:
                sum_inner += tmp * 3
            else:
                return 0
    return sum_inner


result = 0
for i in arr:
    bracket = checkBracket(i)
    if bracket & 1:  # 닫는 괄호
        result += calStack(stack, bracket)
    else:
        stack.append(i)

print(result)