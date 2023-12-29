import math

def calc_fee(parked_time, basic_time, basic_fee, per_time, per_fee):
    if parked_time <= basic_time:
        return basic_fee
    
    over_time = math.ceil((parked_time - basic_time) / per_time)
    basic_fee += over_time * per_fee
    
    return basic_fee

def solution(fees, records):
    answer = []
    
    park_arr = {}
    
    park_time = []
    park_num = []
    for record in records:
        t, car_num, stat = record.split(' ')
        # print(t, car_num, stat)
        h, m = map(int, t.split(':'))
        time_to_min = h*60 + m
        
        if stat == 'IN':
            park_time.append(time_to_min)
            park_num.append(car_num)
        else:
            i = park_num.index(car_num)
            in_time_min = park_time.pop(i)
            park_num.pop(i)
            
            parked_time = time_to_min - in_time_min
            
            if car_num not in (park_arr):
                park_arr[car_num] = parked_time
            else:
                park_arr[car_num] += parked_time
    # print(park_time, park_num)
            
    # 남은 차 출차 (23:59)
    for i in range(len(park_num)):
        out_time_min = 23*60 + 59
        in_time_min = park_time.pop()
        car_num = park_num.pop()
        
        parked_time = out_time_min - in_time_min
        
        if car_num not in (park_arr):
            park_arr[car_num] = parked_time
        else:
            park_arr[car_num] += parked_time
            
    # print(park_arr)
    
    fee_arr = []
    for car_num, parked_time in park_arr.items():
        # print(car_num, parked_time)
        fee = calc_fee(parked_time, fees[0], fees[1], fees[2], fees[3])
        fee_arr.append([int(car_num), fee])
        
    fee_arr.sort(key=lambda x: x[0])
    
    for car, fee in fee_arr:
        answer.append(fee)
    
    return answer

if __name__ == "__main__":
    solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])     # return 	[14600, 34400, 5000]