# 영화감독 숌

import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    movie = '666'
    for i in range(1, N):
        while True:
            movie = str(int(movie) + 1)
            if '666' in movie:
                break
    print(movie)

if __name__ == "__main__":
    solution()