#!/usr/bin/env python

def maxMoney(n, k):
    sum = 0
    i = 0
    while i <= n:
        sum += i
        if (sum == k):
            sum = sum - 1
        i += 1
    print sum


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    # print out the result    
maxMoney(n, k)
