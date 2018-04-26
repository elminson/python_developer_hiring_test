# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q3 import calculateScore


class Test(unittest.TestCase):
    def testCalculateScore(self):
        text = 'nothing'
        prefix = 'bruno'
        suffix = 'ingenious'
        expect = 'nothing'
        result = calculateScore(text, prefix, suffix)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
