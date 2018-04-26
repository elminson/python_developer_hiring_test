# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q19 import usernameDisparity


class Test(unittest.TestCase):
    def testUsernameDisparity(self):
        a = 'ababaa'
        expect = 11
        result = usernameDisparity(a)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
