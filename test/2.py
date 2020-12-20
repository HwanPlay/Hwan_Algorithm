import sys
sys.stdin = open('input.txt', 'r')

def solution(N):
    str_N = str(N)
    result = 0xffff * -1
    if N>=0:
        for i in range(len(str_N)+1):
            tmp_str = str_N[:i] + '5' + str_N[i:]
            tmp_int = int(tmp_str)
            if tmp_int > result:
                result = tmp_int
            # print(tmp_str)
    else:
        for i in range(len(str_N)+1):
            tmp_str = str_N[1:1+i] + '5' + str_N[1+i:]
            tmp_int = int(tmp_str) * -1
            if tmp_int > result:
                result = tmp_int
            # print(tmp_str)
    return result

print(solution(int(input())))