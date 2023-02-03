# 진법 변환

def convert(a, b):
    num = ""
    while(a != 0):
        div = a%b
        if div >= 10:
            num = chr(div + 55) + num
        else :
            num = str(div) + num
        a = int(a/b)

    return num

N, B = map(int, input().split())

print(convert(N, B))

# 다른 풀이
# zinsu = [str(x) for x in range(10)] + [chr(x) for x in range(ord('A'), ord('Z')+1)]
# nums = []
# while n > 0:
#     nums.append(zinsu[(n % b)])
#     n = n // b
# print(''.join(nums[::-1]))