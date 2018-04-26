# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q15 import countPowerNumbers


class Test(unittest.TestCase):
    def testCountPowerNumbers1(self):
        l = 0
        r = 1
        expect = 2
        result = countPowerNumbers(l, r)
        self.assertEqual(result, expect)

    def testCountPowerNumbers2(self):
        l = 25
        r = 30
        expect = 5
        result = countPowerNumbers(l, r)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
