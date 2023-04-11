# 완전 탐색 (lv.1)

import sys
input = sys.stdin.readline

def solution(sizes):
    answer = 0
    length = len(sizes)

    sorted_sizes = []
    for size in sizes:
        w, h = size
        if w >= h:
            sorted_sizes.append(size)
        else:
            sorted_sizes.append([h,w])
    # print(sorted_sizes)
    
    max_width_size = max(sorted_sizes, key=lambda x: (x[0],x[1]))
    max_height_size = max(sorted_sizes, key=lambda x: (x[1],x[0]))
    # print(max_width_size, max_height_size)
    max_width = max_width_size[0]
    max_height = max_height_size[1]

    answer = max_width * max_height

    return answer

if __name__ == "__main__":
    solution([[60, 50], [30, 70], [60, 30], [80, 40]])  # return 4000