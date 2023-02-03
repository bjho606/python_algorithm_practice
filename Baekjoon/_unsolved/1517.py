# 버블 소트 (다시)
# divide and conquer

import sys

# 시간초과
def bubble_sort(arr):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1

            # print(arr)

    return count

# 메모리 초과
def merge_sort(arr):
    global count

    if len(arr) == 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    sorted_arr = []
    left_i, right_i = 0, 0
    
    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            sorted_arr.append(left[left_i])
            left_i += 1
        else:
            sorted_arr.append(right[right_i])
            right_i += 1
            count += 1

        sorted_arr += left[left_i:]
        sorted_arr += right[right_i:]

    return sorted_arr

N = int(sys.stdin.readline())

A = list(map(int, sys.stdin.readline().split()))

count = 0
# print(bubble_sort(A))
# merge_sort(A)
merge_sort(0, N)
print(count)