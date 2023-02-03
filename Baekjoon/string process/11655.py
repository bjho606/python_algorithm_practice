# ROT13

import sys

S = sys.stdin.readline()
ans = ""

for letter in S:
    if 'a' <= letter <= 'm' or 'A' <= letter <= 'M':
        letter = chr(ord(letter) + 13)
    elif 'n' <= letter <= 'z' or 'N' <= letter <= 'Z':
        letter = chr(ord(letter) - 13)
    ans += letter

print(ans)