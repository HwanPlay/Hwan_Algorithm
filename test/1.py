import sys
sys.stdin = open('input.txt', 'r')


def solution(S, K):
    # write your code in Python 3.6
    days = ['Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun']
    S_idx = 0
    for idx, day in enumerate(days):
        if S == day:
            S_idx = idx
            break
    return (S_idx+K) % 7
