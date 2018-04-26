# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q11 import superStack


class Test(unittest.TestCase):
    def testSuperStack(self):
        stacks = ['push 4', 'pop', 'push 3', 'push 5',
                  'push 2', 'inc 3 1', 'pop', 'push 1',
                  'inc 2 2', 'push 4', 'pop', 'pop']
        expect = [6, 8]
        result = superStack(stacks)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
