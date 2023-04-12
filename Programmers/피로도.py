# 완전 탐색 (lv.2)

import sys
input = sys.stdin.readline
import itertools

def solution(k, dungeons):
    answer = -1
    dungeon_count = len(dungeons)
    
    for perm_count in range(dungeon_count, 0, -1):
        for dungeon_combination in itertools.permutations(dungeons, perm_count):
            # print(dungeon_combination)
            stress = k
            ans_temp = 0    # 탐험한 던전 수
            for dungeon in dungeon_combination:
                # 최소 피로도 X
                if stress < dungeon[0]:
                    answer = max(ans_temp, answer)
                    break
                ans_temp += 1
                stress -= dungeon[1]
                # print(stress, end= ', ')
            answer = max(ans_temp, answer)
    
    return answer

if __name__ == "__main__":
    solution(80, [[80,20],[50,40],[30,10]])     # return 3