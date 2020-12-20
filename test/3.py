# import sys
# sys.stdin = open('input.txt', 'r')

def solution(S, C):
    if len(S) == 1:
        return 0
    checks = [False] * len(S)
    idx_prev, idx_next = 0, 1
    result = 0
    while idx_next < len(S):
        val_prev, val_next = S[idx_prev], S[idx_next]
        cost_prev, cost_next = C[idx_prev], C[idx_next]
        if val_prev == val_next:
            if cost_prev <= cost_next:
                if checks[idx_prev]:
                    result += cost_next
                    checks[idx_next] = True
                else:
                    result += cost_prev
                    checks[idx_prev] = True
            else:
                result += cost_next
                checks[idx_next] = True
        idx_prev += 1
        idx_next += 1
    return result

print(solution("ccacc", [6,5,6,6,3]))