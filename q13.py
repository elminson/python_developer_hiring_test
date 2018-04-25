#!/usr/bin/env python


def stockmax(prices):
    price = 0
    cost = 0
    income = 0
    for i in xrange(len(prices)-1,-1,-1):
        if price < prices[i]:
            price = prices[i]
        else:
            cost += prices[i]
            income += price
    return income-cost


if __name__ == "__main__":
    t = int(raw_input().strip())
    for a0 in xrange(t):
        n = int(raw_input().strip())
        prices = map(int, raw_input().strip().split(' '))
        result = stockmax(prices)
        print result

