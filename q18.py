#!/usr/bin/env python


def findNewIndex(max_index, min_index, input_array):
    input_array.pop(min_index)

    num = min(input_array)
    min_index = input_array.index(num)

    if max_index > min_index:
        return input_array[max_index] - input_array[min_index]
    elif max_index < min_index and input_array:
        return findNewIndex(max_index, min_index, input_array)
    else:
        return -1


def maxDifference(input_array):
    max_num = max(input_array)
    max_index = input_array.index(max_num)

    min_num = min(input_array)
    min_index = input_array.index(min_num)

    if max_index > min_index:
        print input_array[max_index] - input_array[min_index]
    else:
        ans = findNewIndex(max_index, min_index, input_array)
        print ans


if __name__ == '__main__':
    input_array = list()
    for _ in range(input()):
        input_array.append(input())
    maxDifference(input_array)
