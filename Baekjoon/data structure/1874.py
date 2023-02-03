# 스택 수열

import sys
input = sys.stdin.readline

n = int(input())
st = []
li = []
count = 1
flag = True

for i in range(n):
    num = int(input())

    while count <= num:
        li.append(count)
        st.append('+')
        count += 1
    if li[-1] == num:
        li.pop()
        st.append('-')
    else:
        flag = False

if flag:
    for i in st:
        print(i)
else:
    print('NO')