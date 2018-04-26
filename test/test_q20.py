# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q20 import *


class Test(unittest.TestCase):
    def testMain(self):
        expect = None
        result = main()
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
