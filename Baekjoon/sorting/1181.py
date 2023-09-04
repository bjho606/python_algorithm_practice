# 단어 정렬

import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    word_list = []

    for _ in range(N):
        word = input().strip()
        # print(word)
        word_list.append((word, len(word)))
    
    word_list.sort(key=lambda x: (x[1], x[0]))
    # print(word_list)

    dup_word = ''
    for _ in range(N):
        if word_list[_][0] == dup_word:
            continue
        else:
            print(word_list[_][0])
            dup_word = word_list[_][0]

if __name__ == "__main__":
    solution()