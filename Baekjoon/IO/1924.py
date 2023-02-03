# 요일

import sys

weeks = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, sys.stdin.readline().split())

count = 0

for month in range(1, x):
    # print(month)
    count += days[month-1]

count += y - 1

print(weeks[count % 7])

# 다른 풀이
# import datetime
# import sys
# M,D = sys.stdin.readline().split()
# str_datetime = '2007' +'-'+ M + '-' + D
# format = '%Y-%m-%d'
# dt_datetime = datetime.datetime.strptime(str_datetime,format)
# print(dt_datetime.strftime('%a').upper())