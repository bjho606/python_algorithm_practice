# 문자열 분석

import sys

while(True):
    line = sys.stdin.readline().rstrip('\n')
    lower, upper, num, blank = 0, 0, 0, 0

    if not line:
        break
    for letter in line:
        if letter.islower():
            lower += 1
        elif letter.isupper():
            upper += 1
        elif letter.isnumeric():
            num += 1
        elif letter == ' ':
            blank += 1
    # lower = sum([int(letter.islower()) for letter in line])
    # upper = sum([int(letter.isupper()) for letter in line])
    # num = sum([int(letter.isnumeric()) for letter in line])
    # blank = sum([int(letter == ' ') for letter in line])

    print(lower, upper, num, blank)