def solution(s):
    answer = len_s = len(s)

    for tmp_len in range(1, len_s // 2 + 1):
        result_len = 0
        num_stack = 1
        prev_text = ''
        for j in range(len_s):
            tmp_next = tmp_len * (j+1)
            tmp_prev = tmp_len * j

            if tmp_next == len_s:
                tmp_text = s[tmp_prev: tmp_next]
                if prev_text == tmp_text:
                    result_len += len(str(num_stack)) + tmp_len
                else:
                    result_len += tmp_len * 2
                break
            elif tmp_next > len_s > tmp_prev:
                result_len += len_s - tmp_prev + tmp_len
                break

            tmp_text = s[tmp_prev: tmp_next]
            if prev_text == '':
                prev_text = tmp_text
            else:
                if prev_text == tmp_text:
                    num_stack += 1
                else:
                    if num_stack == 1:
                        result_len += tmp_len
                    else:
                        result_len += len(str(num_stack)) + tmp_len
                    prev_text = tmp_text
                    num_stack = 1
        if answer > result_len:
            answer = result_len
    return answer

import sys
sys.stdin = open('input.txt', 'r')

print(solution(input()))