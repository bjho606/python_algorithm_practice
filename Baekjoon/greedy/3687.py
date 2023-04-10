# 성냥개비
import sys
input = sys.stdin.readline

match_set = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6} # 숫자당 필요한 성냥 개수

n = int(input())

# dp 값은 나올 수 있는 가장 큰 숫자
dp_max = [0]*101
dp_min = [0]*101

# 최대값
dp_max[2] = 1
dp_max[3] = 7
for i in range(4, 101):
    # 짝수면 최대값은 11..11
    if i % 2 == 0:
        max_temp = '1' * (i//2)
    # 홀수면 최대값은 71..1
    else:
        max_temp = '7' + '1' * (i//2 -1)
    dp_max[i] = int(max_temp)

# 최소값
min_match_num = {2:1, 3:7, 4:4, 5:2, 6:6, 7:8}   # 성냥 개수당 가장 작은 숫자

dp_min[2] = 1
dp_min[3] = 7
dp_min[4] = 4
dp_min[5] = 2
dp_min[6] = 6
dp_min[7] = 8
dp_min[8] = 10
dp_min[9] = 18
dp_min[10] = 22
for i in range(11, 101):
    min_temp = '8' * (i//7)

    leftover = i % 7
    if leftover == 1:
        min_temp = '10' + min_temp[1:]
    elif leftover == 2:
        min_temp = '1' + min_temp
    elif leftover == 3:
        # min_temp = '22' + min_temp[1:]
        min_temp = '200' + min_temp[2:]
    elif leftover == 4:
        min_temp = '20' + min_temp[1:]
    elif leftover == 5:
        min_temp = '2' + min_temp
    elif leftover == 6:
        min_temp = '6' + min_temp
    
    dp_min[i] = int(min_temp)
    
for _ in range(n):
    match = int(input())
    print(dp_min[match], end=' ')
    print(dp_max[match])