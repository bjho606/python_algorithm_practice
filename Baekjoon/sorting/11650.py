# 좌표 정렬하기

import sys

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    sorted_array = []
    left_i = right_i = 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i][0] < right[right_i][0]:
            sorted_array.append(left[left_i])
            left_i += 1    
        elif left[left_i][0] > right[right_i][0]:
            sorted_array.append(right[right_i])
            right_i += 1
        elif left[left_i][0] == right[right_i][0]:
            if left[left_i][1] <= right[right_i][1]:
                sorted_array.append(left[left_i])
                left_i += 1
            else:
                sorted_array.append(right[right_i])
                right_i += 1

    while left_i < len(left):
        sorted_array.append(left[left_i])
        left_i += 1
    while right_i < len(right):
        sorted_array.append(right[right_i])
        right_i += 1

    return sorted_array

N = int(sys.stdin.readline())

array = []
for i in range(N):
    [x,y] = map(int, sys.stdin.readline().split())
    array.append([x,y])

# -- sorting --
# array.sort()
array = merge_sort(array)

# -- printing --
for i in range(N):
    print(array[i][0], array[i][1])