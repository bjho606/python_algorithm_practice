def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    sorted_array = []

    left_i, right_i = 0, 0

    while left_i < len(left) and right_i < len(right):
        if left[left_i] < right[right_i]:
            sorted_array.append(left[left_i])
            left_i += 1
        else:
            sorted_array.append(right[right_i])
            right_i += 1

    sorted_array += left[left_i:]
    sorted_array += right[right_i:]

    return sorted_array

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# numbers.sort()
min = numbers[0]

numbers = merge_sort(numbers)

for number in numbers:
    print(number)