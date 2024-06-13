# LCS

import sys
input = sys.stdin.readline

""" first thought
모든 부분 수열을 구해서 (set) 서로 둘다 있는 것 중에 최대..?
"""

def solution():
    str1 = list(input().strip())
    str2 = list(input().strip())
    len1 = len(str1)
    len2 = len(str2)
    
    set1 = []
    set2 = []
    
    def getSets(arr, sets, cur_str, index, end):
        if index == end:
            return sets
        
        if cur_str + arr[index] not in sets:
            sets.append(cur_str+arr[index])
        
        sets = getSets(arr, sets, cur_str, index+1, end)
        sets = getSets(arr, sets, cur_str+arr[index], index+1, end)

        return sets

    set1 = getSets(str1, set1, '', 0, len1)
    set2 = getSets(str2, set2, '', 0, len2)
    # print(set1)
    set1 = sorted(set1, key=lambda x: -len(x))

    for ls in set1:
        if ls in set2:
            # print(ls)
            print(len(ls))
            break

if __name__ == "__main__":
    solution()