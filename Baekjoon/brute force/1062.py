# 가르침

from itertools import combinations
import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())

    learned_alphabet = {'a', 'n', 't', 'c', 'i'}

    words = []
    not_learned_alphabet = set()
    for i in range(N):
        word = set(input().rstrip('\n'))
        word -= learned_alphabet
        not_learned_alphabet |= word
        words.append(word)
    # print(words)
    # print(not_learned_alphabet)

    K -= 5
    if K < 0:
        print(0)
        exit()
    
    if len(not_learned_alphabet) <= K:
        print(N)
        exit()

    max_count = 0
    for learn in combinations(not_learned_alphabet, K):
        count = 0
        learned = set(learn)
        # print(learned)

        for word in words:
            if word == word & learned:
                count += 1

        max_count = max(max_count, count)

    print(max_count)

if __name__ == "__main__":
    solution()