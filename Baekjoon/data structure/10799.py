# 쇠막대기 (불안)

import sys
input = sys.stdin.readline

ip = input().strip()
st = []
stick = 0

for i, letter in enumerate(ip):
    if letter == '(':
        st.append(letter)
    else:
        if ip[i-1] == '(':
            st.pop()
            stick += st.count('(')
        else:
            st.pop()
            stick += 1

print(stick)