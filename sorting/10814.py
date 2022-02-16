# 나이순 정렬

import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    l_index = r_index = 0
    merged_arr = []

    while l_index < len(left) and r_index < len(right):
        if left[l_index][0] <= right[r_index][0]:
            merged_arr.append(left[l_index])
            l_index += 1
        elif left[l_index][0] > right[r_index][0]:
            merged_arr.append(right[r_index])
            r_index += 1

    while l_index < len(left):
        merged_arr.append(left[l_index])
        l_index += 1
    while r_index < len(right):
        merged_arr.append(right[r_index])
        r_index += 1

    return merged_arr

arr = []

N = int(sys.stdin.readline())
for i in range(N):
    age, name = sys.stdin.readline().split()
    age = int(age)
    arr.append([age, name])

arr = merge_sort(arr)

for i in range(N):
    print(arr[i][0], arr[i][1])