# DFS/BFS lv.2

import sys
input = sys.stdin.readline
import itertools

def dfs(numbers, i, cur_sum, target, answer):
    if i >= len(numbers):
        # print(cur_sum)
        if cur_sum == target:
            answer += 1
        return answer
        
    for calc in (1,-1):
        numbers[i] = numbers[i] * calc
        cur_sum += numbers[i]
        answer = dfs(numbers, i+1, cur_sum, target, answer)
        cur_sum -= numbers[i]
    
    return answer

def solution(numbers, target):
    answer = 0
    
    answer = dfs(numbers, 0, 0, target, answer)
    # print(answer)
    
    return answer

if __name__ == "__main__":
    solution([4, 1, 2, 1], 4)   # return 2