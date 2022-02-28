# 암호 코드

import sys

code = list(map(int, sys.stdin.readline().rstrip('\n')))
# print(code)

dp = [0 if num > 0 else 0 for num in range(len(code)+1)]
if code[0] == 0:
    print(0)
    exit()

code = [0] + code
dp[0] = dp[1] = 1

for i in range(2, len(code)):
    if code[i] > 0:
        dp[i] += dp[i-1]
    if 10 <= code[i-1]*10 + code[i] <= 26:
        dp[i] += dp[i-2]

print(dp[len(code)-1] % 1000000)