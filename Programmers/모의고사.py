# 완전 탐색 (lv.1)

import sys
input = sys.stdin.readline

def solution(answers):
    answer = []
    
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    one_count = 0
    two_count = 0
    three_count = 0
    
    for i, num in enumerate(answers):
        one_count += one[i%5] == num
        two_count += two[i%8] == num
        three_count += three[i%10] == num
        
    rank = [[1,one_count], [2,two_count], [3,three_count]]
    rank.sort(key= lambda x:(-x[1],x[0]))
    
    answer.append(rank[0][0])
    
    max_num = rank[0][1]
    for i in range(1, 3):
        if rank[i][1] == max_num:
            answer.append(rank[i][0])
    
    return answer

if __name__ == "__main__":
    solution([1,3,2,4,2])   # return [1,2,3]