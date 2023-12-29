# 최빈수 구하기 (정렬)

import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    T_num = int(input())
    scores = list(map(int, input().split()))
    # print(scores)

    answer = scores[0]

    score_dict = {}

    for score in scores:
        if score not in score_dict:
            score_dict[score] = 1
        else:
            score_dict[score] += 1
    
    sorted_score_dict = sorted(score_dict.items(), key=lambda x:(-x[1], -x[0]))
    # print(sorted_score_dict)
    
    answer = sorted_score_dict[0][0]

    print(f'#{test_case} {answer}')