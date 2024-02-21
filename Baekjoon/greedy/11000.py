# 강의실 배정

import sys
import heapq
input = sys.stdin.readline

"""
의식의 흐름 (물론 혼자 못 풀었었음)
1. 시간이 정렬이 필요한건 확실한듯 -> 그럼 무슨 기준으로??
2. 일단 시작 시간으로 해보자
3. 새로운 강의실을 만들 때마다 추가할 강의실 배열을 만들자 -> 어떻게 추가할 것인가? 시작,끝 시간 전부? 시작 시간? 끝 시간?
4. 어차피 타임라인이 정렬되어 있기 때문에, 결국 비교해야할 것은 이전의 '끝' 시간 vs 새로 추가할 강의의 '시작' 시간 => 끝 시간을 배열에 추가하자
5. 새로운 시작 시간이 들어올 때, 강의실의 '가장 일찍 끝나는 끝 시간'과 비교하자
6. 품을 수 있으면, 그 끝 시간을 새로 들어온 강의의 끝 시간으로 갱신. 안되면 새로운 강의실 추가
[정리]
1) 타임 라인을 시작 시간으로 정렬
2) 비교할 땐, 시작 시간 vs 끝 시간.
3) 추가할 땐, 끝 시간
"""

def solution():
    N = int(input())
    classes = []

    for i in range(N):
        classes.append(list(map(int, input().split())))
    # print(classes)
    classes = sorted(classes)
    
    rooms = [classes[0][1]]

    for i in range(1, N):
        start, end = classes[i]
        if rooms[0] <= start:
            heapq.heappop(rooms)
        heapq.heappush(rooms, end)

    # [84%에서 시간초과..]
    # rooms = []
    # for start, end in classes:
    #     if not rooms:
    #         rooms.append(end)
    #     else:
    #         updatable = False
    #         for i, room_end in enumerate(rooms):
    #             if start >= room_end:
    #                 rooms[i] = end
    #                 updatable = True
    #                 break

    #         if not updatable:
    #             rooms.append(end)

    print(len(rooms))

if __name__ == "__main__":
    solution()