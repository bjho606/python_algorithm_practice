# 주유소

import sys

input = sys.stdin.readline

N = int(input())
roads = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0] * roads[0]

min_city = 0
for cur_city in range(1, N-1):
    if prices[min_city] > prices[cur_city]:
        min_city = cur_city
    min_price += prices[min_city] * roads[cur_city]

print(min_price)