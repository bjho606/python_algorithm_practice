# 작업

import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    times = [0] * (N+1)
    relevant = {}

    for job in range(1, N+1):
        t = list(map(int, input().split()))
        times[job] = t[0]
        for rjob in t[2:]:
            if job in relevant:
                relevant[job].append(rjob)
            else:
                relevant[job] = [rjob]
    # print(relevant)

    for job in range(1, N+1):
        if job in relevant:
            sum_time = 0
            for rjob in relevant[job]:
                sum_time = max(sum_time, times[rjob])

            times[job] += sum_time
    
    print(max(times))

if __name__ == "__main__":
    solution()