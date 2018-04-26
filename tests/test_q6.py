# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q6 import calculateMaximumProfit


class Test(unittest.TestCase):
    def testCalculateMaximumProfit(self):
        cost_per_cut = 1
        metal_price = 10
        lengths_array = [26, 103, 59]
        expect = 1770
        result = calculateMaximumProfit(cost_per_cut, metal_price, lengths_array)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
