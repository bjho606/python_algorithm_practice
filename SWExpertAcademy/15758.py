T = int(input())
for test_case in range(1, T + 1):
    str1, str2 = map(str, input().split())
    print('#'+str(test_case), end=' ')

    len1 = len(str1)
    len2 = len(str2)

    str1 = str1 * len2
    str2 = str2 * len1
    # print(str1, str2)

    if str1 == str2:
        print('yes')
    else:
        print('no')