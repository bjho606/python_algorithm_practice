# 완전 탐색 (lv.2)

import sys
input = sys.stdin.readline

def solution(brown, yellow):
    answer = []
    # 2x+2y-4 = brown
    # (x-2) * (y-2) = yellow
    # x*y = brown+yellow

    carpet = brown+yellow
    width = 0
    height = 0
    
    for h in range(1, carpet+1):
        if carpet % h == 0:
            w = carpet // h
            if (2*w + 2*h - 4 == brown) and ((w-2) * (h-2) == yellow):
                width = w
                height = h
                break
    
    answer.append(width)
    answer.append(height)
    
    return answer

if __name__ == "__main__":
    solution(10, 2) # return [4,3]