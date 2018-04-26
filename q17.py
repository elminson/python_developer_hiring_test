#!/usr/bin/env python

from fractions import Fraction


def reducedFractionSums(fracs):
    b = fracs[0].split('+')
    c0 = map(int, b[0].split('/'))
    c1 = map(int, b[1].split('/'))
    t = Fraction(c0[0], c0[1]) + Fraction(c1[0], c1[1])
    return (str(t.numerator) + '/' + str(t.denominator))
    fracs.pop()


def main():
    fracs = list()
    for _ in range(input()):
        fracs.append(raw_input())
        print reducedFractionSums(fracs)


if __name__ == '__main__':
    main()
