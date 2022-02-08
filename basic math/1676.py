# 팩토리얼 0의 개수

N = int(input())

facto = 1
if N == 0 or N == 1:
    print(0)
else:
    for i in range(1, N+1):
        facto *= i
    
    facto = str(facto)
    count = 0
    for i in reversed(facto):
        if i == '0':
            count += 1
        else: break
    print(count)