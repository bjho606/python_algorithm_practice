import sys
import itertools
input = sys.stdin.readline

def getCrossXY(a1,b1,c1, a2,b2,c2):
    # a1,b1,c1 = line1
    # a2,b2,c2 = line2

    x = (b1*c2 - c1*b2) / (a1*b2 - b1*a2)
    y = (c1*a2 - a1*c2) / (a1*b2 - b1*a2)

    return x, y    

def isXYInt(x, y):
    isXInt = int(x) == x
    isYInt = int(y) == y

    if isXInt and isYInt:
        return True
    else:
        return False

def solution(line):
    answer = []
    line_count = len(line)
    xy_arr = []
    
    for line1, line2 in itertools.combinations(line, 2):
        a1,b1,c1 = line1
        a2,b2,c2 = line2

        # 평행하는지 체크
        if (a1*b2 - b1*a2) == 0:
            continue

        x, y = getCrossXY(a1,b1,c1, a2,b2,c2)

        if isXYInt(x, y):
            xy_arr.append((int(x),int(y)))
    # print(xy_arr)

    max_y = max(xy_arr, key=lambda x:x[1])[1]
    min_y = min(xy_arr, key=lambda x:x[1])[1]
    # print(max_y, min_y)
    max_x = max(xy_arr, key=lambda x:x[0])[0]
    min_x = min(xy_arr, key=lambda x:x[0])[0]
    x_len = max_x - min_x + 1

    for i in range(max_y, min_y-1, -1):
        ans_line = ''
        # print("\"", end='')
        for j in range(min_x, max_x+1):
            if (j, i) in xy_arr:
                # print('*', end='')
                ans_line += '*'
            else:
                # print('.', end='')
                ans_line += '.'
        # print("\"")
        answer.append(ans_line)

    # print(answer)
    return answer

if __name__ == "__main__":
    ex = [[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]
    solution(ex)