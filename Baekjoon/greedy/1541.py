# 잃어버린 괄호

import sys

input = sys.stdin.readline

question = input().rstrip('\n')
parts = question.split('-')
# print(parts)
answer = 0
for i, part in enumerate(parts):
    part_sum = 0
    numbers = list(map(int, part.split('+')))
    # print(numbers)
    for number in numbers:
        part_sum += number
    
    if i == 0:
        answer += part_sum
    else:
        answer -= part_sum

print(answer)