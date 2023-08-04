# 방 번호

import sys
input = sys.stdin.readline

# print(num_set)

N = input().rstrip('\n')

num_dict = {
    '0': 1,
    '1': 1,
    '2': 1,
    '3': 1,
    '4': 1,
    '5': 1,
    '6': 1,
    '7': 1,
    '8': 1,
    '9': 1
}
count = 1
for num in N:
    if num_dict[num] < 1:
        # 6 or 9 예외처리
        if num == '6':
            if num_dict['9'] >= 1:
                num_dict['9'] -= 1
                continue
        elif num == '9':
            if num_dict['6'] >= 1:
                num_dict['6'] -= 1
                continue

        count += 1
        for key in num_dict.keys():
            num_dict[key] += 1
    num_dict[num] -= 1

print(count)