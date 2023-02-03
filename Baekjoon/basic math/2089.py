# -2진수

mogc = int(input())
two = ''

if mogc == 0:
    two = '0'
    print(two)
    exit()

while mogc != 0:
    div = mogc % -2
    if div == 0:
        two = '0' + two
        mogc //= -2
    else:
        two = '1' + two
        mogc = mogc // -2 + 1

print(two)