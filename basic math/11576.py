# base conversion

def converter(list_val, A, B):
    ten = 0
    for i, val in enumerate(list_val):
        ten += int(val * A**(len(list_val)-1-i))
    # print(ten)

    converted_value = ''
    while ten:
        converted_value = ' ' + str(ten%B) + converted_value
        ten = ten // B

    return converted_value.strip()

A, B = map(int, input().split())
m = int(input())
# for i in range(m):
list_val = list(map(int, input().split()))
# print(list_val)
print(converter(list_val, A, B))