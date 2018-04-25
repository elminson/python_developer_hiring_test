#!/usr/bin/env python
from itertools import izip


def get_similarity(a, suffix):
    score = 0
    for a, b in izip(a, suffix):
        if a != b:
            break
        score += 1
    return score


def usernameDisparity(a):
    answer = i = 0
    while i < len(a):
        suffix = a[i:]
        answer += get_similarity(a, suffix)
        i += 1
    print answer


if __name__ == '__main__':
    for _ in range(input()):
        a = raw_input()
        usernameDisparity(a)