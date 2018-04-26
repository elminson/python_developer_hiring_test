# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q13 import stockmax


class Test(unittest.TestCase):
    def testStockmax(self):
        prices = [1, 2, 100]
        expect = 197
        result = stockmax(prices)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
