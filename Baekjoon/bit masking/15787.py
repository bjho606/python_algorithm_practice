# 기차가 어둠을 헤치고 은하수를

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())

    trains = [0] * N

    for i in range(M):
        command = list(map(int, input().rstrip('\n').split()))

        if command[0] == 1:
            trains[command[1]-1] |= 1 << command[2] - 1
        elif command[0] == 2:
            trains[command[1]-1] &= ~(1 << command[2] - 1)
        elif command[0] == 3:
            trains[command[1]-1] = trains[command[1]-1] << 1
            trains[command[1]-1] &= ~(1 << 20)
        elif command[0] == 4:
            trains[command[1]-1] = trains[command[1]-1] >> 1
    # print(trains)

    print(len(set(trains)))

if __name__ == "__main__":
    solution()