#!/usr/bin/env python


def calculateMaximumProfit(cost_per_cut, metal_price, lengths):
    maxProfit = 0
    curProfit = 0
    maxLength = 0
    totalRods = 0
    totalCuts = 0

    #  Find out maximum length
    for curLength in lengths:
        maxLength = max(maxLength, curLength)

    #  For each of the possible rod lengths, calculate possible profit
    curLength = 1
    while curLength < maxLength:
        totalRods = 0
        totalCuts = 0
        #  Cut each of the rods into smaller rods of size curLength
        #  Count total rods and total cuts
        for length in lengths:
            totalRods += (length / curLength)
            totalCuts += ((length - 1) / curLength)
        #  Calculate current profit
        curProfit = totalRods * curLength * metal_price - totalCuts * cost_per_cut
        #  Calculate maximum profit
        maxProfit = max(maxProfit, curProfit)
        curLength += 1
    # prints maximum profit
    return maxProfit


def main():
    cost_per_cut = int(input())
    metal_price = int(input())
    # array input of metals length
    lengths_array = list()
    lengths_count = int(input())

    for i in range(int(lengths_count)):
        n = input()
        lengths_array.append(int(n))
        # print out the result
    print calculateMaximumProfit(cost_per_cut, metal_price, lengths_array)


if __name__ == '__main__':
    main()
