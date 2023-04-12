# 완전 탐색 (lv.2)

import sys
input = sys.stdin.readline

def solution(word):
    answer = 1
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    next_word = 'A'
    
    while True:
        # 아직 못 찾음
        if next_word < word:
            answer += 1
            # 길이 5 이하면 'A' 추가
            if len(next_word) < 5:
                next_word += 'A'
            # 길이 5 이상이면
            else:
                # print(next_word)
                # 끝 글자(U) 이면 이전 자리수 확인 
                if next_word[-1] == 'U':
                    while next_word[-1] == 'U':
                        next_word = next_word[:-1]
                # 아니면 다음 알파벳
                last_letter = next_word[-1]
                next_word = next_word[:-1] + alpha[alpha.index(last_letter) + 1]
        else:
            break
    
    print(answer)
    return answer

if __name__ == "__main__":
    solution("AAAE")    # return 10