# 팰린드롬수

import sys
input = sys.stdin.readline

def solution():
    while True:
        ip = input().rstrip()
        if ip == '0':
            break

        ip = list(ip)
        num_length = len(ip)
        num_stack = []
        for i in range(num_length//2):
            num_stack.append(ip.pop(0))

        if num_length % 2 == 1:
            ip.pop(0)
        
        flag = True
        for i in range(num_length//2):
            if num_stack.pop() != ip.pop(0):
                print('no')
                flag = False
                break
        if flag:
            print('yes')

    # while True:
    #     n=input()
    #     if n=="0":
    #         break
    #     if n==n[::-1]:
    #         print("yes")
    #     else: print("no")


if __name__ == "__main__":
    solution()