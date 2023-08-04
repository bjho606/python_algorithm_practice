# AC

import sys
input = sys.stdin.readline

T = int(input().rstrip('\n'))
for _ in range(T):
    p = input().rstrip('\n')
    n = int(input().rstrip('\n'))
    str_arr = input().rstrip('\n')
    arr = []
    if n != 0:
        arr = str_arr[1:-1].split(',')
    # print(arr)
    
    # error = False
    # for i in p:
    #     if i == 'R':
    #         arr.reverse()
    #     elif i == 'D':
    #         if not arr:
    #             print('error')
    #             error = True
    #             break
    #         else:
    #             arr.pop(0)

    # if not error:
    #     # print(arr)
    #     if arr:
    #         answer = '[' + ','.join(arr) + ']'
    #     else:
    #         answer = '[]'
    #     print(answer)

    is_reversed = False
    d_count = 0
    error = False
    for i in p:
        if i == 'R':
            is_reversed = not is_reversed
        elif i == 'D':
            if not arr:
                print('error')
                error = True
                break

            if is_reversed:
                arr.pop()
            else:
                arr.pop(0)
    
    if not error:
        if arr:
            if is_reversed:
                arr.reverse()
            answer = '[' + ','.join(arr) + ']'
        else:
            answer = '[]'
        print(answer)