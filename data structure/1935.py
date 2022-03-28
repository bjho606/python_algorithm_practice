# 후위 표기식2

import sys
input = sys.stdin.readline

N = int(input())
ip = input().rstrip('\n')

dict = {}
for i in range(N):
    val = int(input())
    alpha = chr(i + ord('A'))
    # print(alpha)
    dict[alpha] = val

# print(dict)
st = []
for i in ip:
    if 'A' <= i <= 'Z':
        st.append(dict[i])
    else:
        str1 = st.pop()
        str2 = st.pop()

        if i == '+':
            st.append(str2+str1)
        elif i == '-':
            st.append(str2-str1)
        elif i == '*':
            st.append(str2*str1)
        elif i == '/':
            st.append(str2/str1)

print('%.2f' %st[0])