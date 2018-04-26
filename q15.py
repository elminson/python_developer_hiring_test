#!/usr/bin/env python


def countPowerNumbers(l,r):
    count = 0
    i = 2
    a = [False for k in range(r+1)]
    # Since 0,1 can always be represented as a power number
    a[0] = a[1] = True

    while pow(i, 2) <= r:
        j = 2
        while pow(i, j) <= r:
            t = pow(i, j)
            a[t] = True
            j += 1
        i += 1
    i = l
    while i <= r:
        # Since a power number can be represented as sum of two another
        if a[i] == 1:
            count += 1
        else:
            j = i-1
            while j > 0:
                if a[j] == 1 and a[i-j] == 1:
                    count += 1
                    break
                j -= 1
        i += 1

    return count


def main():
    l = int(raw_input().strip())
    r = int(raw_input().strip())
    print countPowerNumbers(l, r)


if __name__ == "__main__":
    main()
