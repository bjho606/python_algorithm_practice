import sys
input = sys.stdin.readline

pc_msg = input().rstrip('\n')
pc_key = input().rstrip('\n')

board = []
# 일파벳 따지기
alpha = dict()
for i in range(ord('A'), ord('Z')+1):
    alpha[chr(i)] = 0
# J 제외
alpha.pop('J')

# 1. 표 채우기 
line = []
# 키로 표 채우기
for letter in pc_key:
    # 아직 사용 안했으면
    if alpha[letter] == 0:
        # 1줄 (5개) 아직 안 채웠으면
        if len(line) < 5:
            line.append(letter)
        # 1줄 채웠으면 줄 바꾸기
        else:
            board.append(line)
            line = []
            line.append(letter)
        
        # 알파벳 사용했다고 표시
        alpha[letter] = 1

# 안 쓴 알파벳으로 표 채우기
for left_alpha in alpha.keys():
    # 안 쓴 알파벳이면
    if alpha[left_alpha] == 0:
        # 1줄 아직 안 채웠으면
        if len(line) < 5:
            line.append(left_alpha)
        # 1줄 채웠으면 줄 바꾸기
        else:
            board.append(line)
            line = []
            line.append(left_alpha)

        alpha[letter] = 1
if line:
    board.append(line)

# print(board)

# 2. 메시지 두 글자씩 나누기
pairs = []
pair = ''
for i, letter in enumerate(pc_msg):
    # 새로운 글자면 그냥 추가
    if pair == '':
        pair += letter
    else:
        # 한 글자만 있으면 조건 따지기
        # 새로운 글자가 같으면
        if letter == pair:
            # 기존 글자가 X면 Q 추가
            if pair == 'X':
                pair += 'Q'
            # 기존 글자가 X가 아니면 X 추가
            else:
                pair += 'X'
            # 두 글자가 완성되었으니 추가하고 새로운 글자로 초기화
            pairs.append(pair)
            pair = letter
        # 새로운 글자가 다르면
        else:
            pair += letter
            # 두 글자가 완성되었으니 추가하고 초기화
            pairs.append(pair)
            pair = ''
# 아직 글자가 남아있다면 'X' 추가하기
if pair != '':
    pairs.append(pair + 'X')
# print(pairs)

# 3. 암호화하기 
encrypt_msg = ''
for pair in pairs:
    # 두 쌍들의 행, 열 구하기
    x1, y1, x2, y2 = -1, -1, -1, -1
    for i in range(5):
        for j in range(5):
            if board[i][j] == pair[0]:
                x1, y1 = i, j
            if board[i][j] == pair[1]:
                x2, y2 = i, j

    # 1) 같은 행이면
    if x1 == x2:
        y1 = (y1+1) % 5
        y2 = (y2+1) % 5
    # 2) 같은 열이면
    elif y1 == y2:
        x1 = (x1+1) % 5
        x2 = (x2+1) % 5
    # 3) 다 다르면
    else:
        tempy = y1
        y1 = y2
        y2 = tempy

    encrypt_msg += board[x1][y1] + board[x2][y2]

print(encrypt_msg)