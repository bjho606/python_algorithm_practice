# 좋다

import sys
input = sys.stdin.readline

"""
1. N <= (2*10)^3 => 완탐은 N^3 (> 10^9) => ㄴㄴ
2. A <= 10^9 => 무섭.. 계산이 안되는게 있나..?
3. 감이 안 잡힘.. 알고리즘 분류 참고..
  정렬 -> 투 포인터..? 
"""

def solution():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    ans = 0
    
    for i in range(N):
        target = A[i]

        left, right = 0, N-1

        while left < right:
            check = A[left] + A[right]
            if check > target:
                right -= 1
            elif check < target:
                left += 1
            else:
                if i != left and i != right:
                    ans += 1
                    break
                elif left == i:
                    left += 1
                elif right == i:
                    right -= 1

    print(ans)


if __name__ == "__main__":
    solution()
