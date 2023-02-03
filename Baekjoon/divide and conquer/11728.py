# 배열 합치기

import sys

# 2. dq (function)
def dq(arr):
    if len(arr) == 1:
        return arr
    
    mid = len(arr) // 2
    left = dq(arr[:mid])
    right = dq(arr[mid:])

    sorted_arr = []
    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] <= right[right_i]:
            sorted_arr.append(left[left_i])
            left_i += 1
        else:
            sorted_arr.append(right[right_i])
            right_i += 1

    sorted_arr += left[left_i:]
    sorted_arr += right[right_i:]

    return sorted_arr

A, B = map(int, sys.stdin.readline().split())
arrA = list(map(int, sys.stdin.readline().split()))
arrB = list(map(int, sys.stdin.readline().split()))

# arr = arrA + arrB
# 1. python
# arr.sort()
# print(*arr)

# 2. dq (시간 초과)
# arr = dq(arr)

arr = []
# 3. two pointer
a_pointer, b_pointer = 0, 0
while a_pointer != len(arrA) and b_pointer != len(arrB):
    if arrA[a_pointer] < arrB[b_pointer]:
        arr.append(arrA[a_pointer])
        a_pointer += 1
    else:
        arr.append(arrB[b_pointer])
        b_pointer += 1

arr += arrA[a_pointer:]
arr += arrB[b_pointer:]

print(*arr)