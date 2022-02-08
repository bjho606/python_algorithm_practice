# 팩토리얼

N = int(input())
if N == 1:
    print(1)
    exit()

facto = 1
for i in range(1, N+1):
    facto *= i

print(facto)