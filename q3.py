#!/usr/bin/env python


def findPreLength(subStr, prefix):
    maximum = 0
    i = 1
    while i < (len(subStr) + 1):
        length = 0
        j = len(prefix) - 1
        string = subStr[0:i]
        k = len(string) - 1

        while j >= 0 and k >= 0:
            if string[k] == prefix[j]:
                length += 1
            else:
                break
            j -= 1
            k -= 1

        if length > maximum and k == -1:
            maximum = length
        i += 1

    return maximum


def findPostLength(subStr, suffix):
    maximum = 0
    i = 0
    while i < len(subStr):
        length = 0
        string = subStr[i:]
        j = k = 0
        while j < len(suffix) and k < len(string):
            if string[k] == suffix[j]:
                length += 1
            else:
                break
            j += 1
            k += 1
        if length > maximum and k == len(string):
            maximum = length

        i += 1
    return maximum


def calculateScore(text, prefix, suffix):
    i = maximum = max_pre = 0
    result = ''
    while i < len(text):
        j = i + 1
        while j <= len(text):
            subStr = text[i:j]
            pre = findPreLength(subStr, prefix)
            post = findPostLength(subStr, suffix)
            pre_post = pre + post
            if maximum < pre_post:
                maximum = pre_post
                result = subStr
                max_pre = pre
            elif maximum == pre_post:
                if pre > max_pre:
                    max_pre = pre
                    result = subStr
            else:
                break

            j += 1
        i += 1
    return result


def main():
    text = str(raw_input().strip())
    prefix = str(raw_input().strip())
    suffix = str(raw_input().strip())
    print calculateScore(text, prefix, suffix)


if __name__ == '__main__':
    main()
