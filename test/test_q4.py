# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q4 import zombieCluster


class Test(unittest.TestCase):
    def testzombieCluster(self):
        zombie_array = ["1100", "1110", "0110", "0001"]
        expect = 2
        result = zombieCluster(zombie_array)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
