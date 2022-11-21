T = int(input())
for test_case in range(1, T+1):
    A, B = map(int, input().split())
    num_length = A + B

    # M, m 구하기
    M, m = '', ''
    if A >= 1:
        M += '1'
        m += '1'
        num_length -= 1

    A -= 1
    a = '1' * A
    b = '0' * B

    M = M + a + b
    m = m + b + a
    # print(M, m)

    # M * m 구하기
    result = bin(int(M,2) * int(m,2))[2:]
    count = result.count('1')
    print('#'+str(test_case),count)
