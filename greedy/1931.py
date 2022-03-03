# 회의실 배정

import sys

N = int(sys.stdin.readline())

meeting = [[0,0] for i in range(N)]
for i in range(N):
    meeting[i][0], meeting[i][1] = map(int, sys.stdin.readline().split())

meeting.sort(key=lambda x:(x[1], x[0]))
# print(meeting)

end_time = meeting[0][1]
count = 1
for i in range(1, N):
    if meeting[i][0] >= end_time:
        count += 1
        end_time = meeting[i][1]

print(count)