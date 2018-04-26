# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q18 import maxDifference


class Test(unittest.TestCase):
    def testMaxDifference(self):
        input_array = [2, 3, 10, 2, 4, 8, 1]
        expect = 8
        result = maxDifference(input_array)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
