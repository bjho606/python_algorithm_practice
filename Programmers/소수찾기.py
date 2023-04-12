# 완전 탐색 (lv.2)

import itertools

def isPrime(num):
    if num == 1 or num == 0:
        return False
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def solution(numbers):
    answer = 0
    
    # isPrime = [0] * 100000000
    # for i in range(1, 100000000, i)
    num_count = len(numbers)
    no_duplicate_num_arr = []
    
    for total_combi_count in range(1, num_count+1):
        for num_combi in itertools.permutations(numbers, total_combi_count):
            # print(num_combi)
            temp = ''
            for str_num in num_combi:
                temp += str_num
            int_num = int(temp)
            if int_num not in no_duplicate_num_arr:
                no_duplicate_num_arr.append(int_num)
            else:
                continue
            # print(int_num)
            if isPrime(int_num):
                print(int_num)
                answer += 1
    
    return answer

if __name__ == "__main__":
    solution("17")  # return 3