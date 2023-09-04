# 마인크래프트

import sys
input = sys.stdin.readline

def solution():
    N, M, B = map(int, input().split())

    final_height = 0
    final_time = sys.maxsize

    ground_arr = []
    for i in range(N):
        ground_arr += list(map(int, input().split()))
    # ground_arr.sort(reverse=True)
    # print(ground_arr)

    # ground_set = set(ground_arr)
    # # print(ground_set)

    # ground_count = []
    # for i in ground_set:
    #     ground_count.append((i, ground_arr.count(i)))
    # ground_count.sort(key=lambda x: (-x[1], -x[0]))
    # # print(ground_count)

    for standard_height in range(257):
        temp_time = 0
        left_block = B

        for block_height in ground_arr:
            if block_height > standard_height:
                temp_time += 2 * (block_height - standard_height)
                left_block += block_height - standard_height
            elif block_height < standard_height:
                temp_time += standard_height - block_height
                left_block -= standard_height - block_height

        if left_block >= 0:
            if temp_time <= final_time:
                final_time = temp_time
                final_height = standard_height

    print(final_time, final_height)

if __name__ == "__main__":
    solution()