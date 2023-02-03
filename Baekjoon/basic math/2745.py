# 진법 변환

jinsu = [str(num) for num in range(10)] + [chr(alpha) for alpha in range(ord('A'), ord('Z')+1)]

N, B = map(str, input().split())
B = int(B)
ans = 0

for i in range(len(N)):
    ans += jinsu.index(N[len(N) - 1 - i]) * B**i

print(ans)

# 다른 풀이
# a, b = input().rstrip().split()
# print(int(a, int(b)))