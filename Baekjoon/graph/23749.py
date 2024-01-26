# 카드컨트롤

import sys
input = sys.stdin.readline

def solution():
    N = int(input())

    card = list(map(str, input().split()))
    # print(card)

    def isWon(arr):
        win = 0
        lose = 0
        i = 0
        while i < 2*N-1:
            # 내 바로 뒤 비교
            if arr[i] == 'O' and arr[i+1] == 'X':
                win += 1
            elif arr[i] == 'X' and arr[i+1] == 'O':
                lose += 1
            
            # # 내 바로 앞 비교
            # if i > 0:
            #     if arr[i] == 'O' and arr[i-1] == 'X':
            #         win += 1
            #     elif arr[i] == 'X' and arr[i-1] == 'O':
            #         lose += 1
                
            i += 2
        # print(win)
        if win > lose:
            return True
        else:
            return False        

    q = []

    if isWon(card):
        print(0)
        return
    else:
        q.append((card, 1)) # 바꿀 배열, 바꾼 횟수
        while True:
            cur_card, count = q.pop(0)

            for i in range(1, 2*N):
                if i == 2*N-1:
                    next_card = [cur_card[i]] + cur_card[:i]
                else:
                    next_card = [cur_card[i]] + cur_card[:i] + cur_card[i+1:]
                if isWon(next_card):
                    print(count)
                    return
                    
                q.append((next_card, count+1))

if __name__ == "__main__":
    solution()