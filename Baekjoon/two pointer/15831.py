# 준표의 조약돌

import sys
input = sys.stdin.readline

def solution():
    N, B, W = map(int, input().split())

    rocks = list(input().rstrip('\n'))

    bcount, wcount = 0, 0

    if rocks[0] == 'B':
        bcount += 1
    else:
        wcount += 1

    max_len = 0
    left, right = 0, 0
    while right < N:
        # 흰 돌 아직 덜 주움
        if wcount < W:
            right += 1
            if right >= N:
                break
            if rocks[right] == 'B':
                bcount += 1
            else:
                wcount += 1
        # 흰 돌은 더 주울 수 있음
        else:
            # 검은 돌 너무 많이 주움
            if bcount > B:
                if rocks[left] == 'B':
                    bcount -= 1
                else:
                    wcount -= 1
                left += 1
            # 검은 돌 아직 더 주울 수 있음
            else:
                max_len = max(max_len, right - left + 1)
                right += 1
                if right >= N:
                    break
                if rocks[right] == 'B':
                    bcount += 1
                else:
                    wcount += 1
    
    print(max_len)

if __name__ == "__main__":
    solution()