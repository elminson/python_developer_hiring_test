# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q17 import reducedFractionSums


class Test(unittest.TestCase):
    def testReducedFractionSums_1(self):
        fracs = ['722/148+360/176']
        expect = '2818/407'
        result = reducedFractionSums(fracs)
        self.assertEqual(result, expect)

    def testReducedFractionSums_2(self):
        fracs = ['978/1212+183/183']
        expect = '365/202'
        result = reducedFractionSums(fracs)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
