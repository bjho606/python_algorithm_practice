# 2진수 8진수

n = input()
# ten = 0
# for i in range(len(n)):
#     ten += int(n[len(n) - 1 - i]) * 2**i
# ans = ""
# while(ten != 0):
#     ans = str(ten%8) + ans
#     ten = int(ten/8)

ten = int(n, 2)
eight = oct(ten)[2:]

print(eight)