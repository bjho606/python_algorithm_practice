# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    
    # 이건 시간초과..
    # pokedex = []
    # for i in range(N):
    #     pokemon = input().rstrip()
    #     pokedex.append(pokemon)
    
    # for i in range(M):
    #     question = input().rstrip()
    #     if '1' <= question[0] <= '9':
    #         print(pokedex[int(question)-1])
    #     else:
    #         print(pokedex.index(question)+1)

    pokedex = {}
    for i in range(N):
        pokemon = input().rstrip()
        pokedex[pokemon] = i+1
        pokedex[str(i+1)] = pokemon
    
    for i in range(M):
        question = input().rstrip()
        print(pokedex[question])

if __name__ == "__main__":
    solution()