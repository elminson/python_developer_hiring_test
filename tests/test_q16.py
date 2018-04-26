# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q16 import minimalCost


class Test(unittest.TestCase):
    def testMinimalCost(self):
        n = 4
        pairs = ['1 2', '1 4']
        expect = 3
        result = minimalCost(n, pairs)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
