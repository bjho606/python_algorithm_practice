import sys

input = sys.stdin.readline

def solution(enroll, referral, seller, amount):
    answer = []
    price = 100
    
    # 인간트리 만들기
    people = {}
    for i, person in enumerate(enroll):
        people[person] = referral[i]
    # print(people)
    
    # 모든 사람 수익 0으로 초기화
    people_result = {}
    for person in enroll:
        people_result[person] = 0
        
    for i, person in enumerate(seller):
        # print(person)
        profit = amount[i] * price
        cascade = profit // 10
        while True:
            # 부모가 없거나 최상위이면 종료
            if person not in people or profit == 0:
                people_result[person] += profit
                break
            if people[person] == '-':
                people_result[person] += profit - cascade
                break

            # print(profit-cascade)
            people_result[person] += profit - cascade

            person = people[person]
            profit = cascade
            cascade = profit // 10
            # print(people_result)
            
    for person in enroll:
        answer.append(people_result[person])
    
    return answer

