# 가운데에서 만나기

import sys
input = sys.stdin.readline
INF = sys.maxsize

def solution():
    N, M = map(int, input().split())
    city_infos = [[INF]*(N+1) for _ in range(N+1)]
    for i in range(N+1):
        city_infos[i][i] = 0

    for _ in range(M):
        a, b, cost = map(int, input().split())
        city_infos[a][b] = cost
    K = int(input())
    living_cities = list(map(int, input().split()))

    for stopover in range(1, N+1):
        for start in range(1, N+1):
            for end in range(1, N+1):
                city_infos[start][end] = min(city_infos[start][end], city_infos[start][stopover] + city_infos[stopover][end])
    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         print(city_infos[i][j], end=" ")
    #     print()
    
    min_dist = INF
    answer = []
    for candidate_city in range(1, N+1):
        max_available_dist = 0
        for friend_city in living_cities:
            forward, backward = city_infos[candidate_city][friend_city], city_infos[friend_city][candidate_city]
            
            if forward == INF or backward == INF: 
                max_available_dist = INF
                break

            if max_available_dist < forward + backward:
                max_available_dist = forward + backward

        if max_available_dist < min_dist:
            min_dist = max_available_dist
            answer = [candidate_city]
        elif max_available_dist == min_dist:
            answer.append(candidate_city)
    print(*answer)

if __name__ == "__main__":
    solution()