# 통계학

import sys
input = sys.stdin.readline

def op1(nums, n):
    return round(sum(nums) / n)

def op2(nums, n):
    return nums[n // 2]

def op3(nums, n):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_count = max(count_dict.values())
    max_count_nums = []
    for d in count_dict:
        if count_dict[d] == max_count:
            max_count_nums.append(d)        
    if len(max_count_nums) > 1:
        return(max_count_nums[1])
    else:
        return(max_count_nums[0])

def op4(nums, n):
    return nums[-1] - nums[0]

N = int(input().rstrip('\n'))
nums = []
for i in range(N):
    nums.append(int(input().rstrip('\n')))
# print(nums)
nums.sort()

# print(round(sum(nums) / N))
# print(nums[N // 2])
# # 최빈값
# count_dict = {}
# for num in nums:
#     if num in count_dict:
#         count_dict[num] += 1
#     else:
#         count_dict[num] = 1
# max_count = max(count_dict.values())
# max_count_nums = []
# for d in count_dict:
#     if count_dict[d] == max_count:
#         max_count_nums.append(d)        
# if len(max_count_nums) > 1:
#     print(max_count_nums[1])
# else:
#     print(max_count_nums[0])
# print(nums[-1] - nums[0])

print(op1(nums, N))
print(op2(nums, N))
print(op3(nums, N))
print(op4(nums, N))