# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q10 import maxMoney


class Test(unittest.TestCase):
    def testMaxMoney(self):
        n = 3
        k = 3
        expect = 5
        result = maxMoney(n, k)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
