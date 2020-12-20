import sys
sys.stdin = open('sample_input.txt', 'r')


def cal_max_benefit(tmp_ms, row, today, benifit):
    if max_benefits[today] < benifit:
        max_benefits[today] = benifit
    for i in range(row, N):
        if arr[i][today] < tmp_ms and arr[i][today] < arr[i][today+1]:
            cal_max_benefit(tmp_ms-arr[i][today], row, today, benifit - arr[i][today] + arr[i][today+1])
    return


for tc in range(int(input())):
    Ms, Ma = map(int, input().split())
    N, L = map(int, input().split())
    tmp_ms = Ms
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    max_benefits = [0]*L
    for i in range(L):
        cal_max_benefit(tmp_ms, 0, i, 0)
        tmp_ms += max_benefits[i] + Ma
    print('#{} {}'.format(tc+1, sum(max_benefits)))