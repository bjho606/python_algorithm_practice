# 평범한 배낭

import sys
input = sys.stdin.readline

# 냅색
# (X)무게별 정렬이 필요
# 해당 무게를 선택 vs 선택X 2가지 경우로 나누어 계산
# 이때, 무게를 선택했을 때 남은 무게를 어떻게 처리?

def solution():
    N, K = map(int, input().split())
    weights = [0]
    values = [0]
    # infos = []
    dp = [[0]*(K+1) for _ in range(N+1)]

    for i in range(N):
        w, v = map(int, input().split())
        weights.append(w)
        values.append(v)
        # infos.append([w, v])
    # print(weights)
    # print(values)
    # sorted_infos = sorted(infos, key=lambda x: (x[0], -x[1]))
    # print(sorted_infos)

    for i in range(1, N+1):             # 모든 가방무게를 볼건데
        for j in range(1, K+1):         # 모든 가능한 무게에 대하여
            if j >= weights[i]:         # 현재 무게가 지금 선택된 가방 무게를 담을 수 있으면
                dp[i][j] = max(values[i] + dp[i-1][j-weights[i]], dp[i-1][j])   # 현재 가방 선택 O (현재 무게 - 현재 가방 무게 의 경우에서의 최대값 + 현재 가방 무게) vs 선택 X
            else:                       # 현재 가방 선택 불가능인 경우
                dp[i][j] = dp[i-1][j]
    # for i in range(1, N+1):
    #     print(dp[i])
    print(dp[N][K])

if __name__ == "__main__":
    solution()