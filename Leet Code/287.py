# leet code 287번
# floyd's tortoise & hare algorithm

def findDuplicate(nums):
    tortoise = nums[0]
    hare = nums[0]
    check_range = len(nums)

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    ptr1 = nums[0]
    ptr2 = hare
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

nums = list(map(int, input().split()))
dup = findDuplicate(nums)
print(dup)