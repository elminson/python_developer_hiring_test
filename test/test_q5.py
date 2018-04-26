# -*- coding: utf-8 -*-
import unittest
import os
import sys

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
sys.path.insert(0, BASEDIR)

from q5 import checkIPs


class Test(unittest.TestCase):
    def testCheckIPsWhenIPWrong(self):
        ip_array = '1213'
        expect = 'Neither'
        result = checkIPs(ip_array)
        self.assertEqual(result, expect)

    def testCheckIPsWhenIPv4(self):
        ip_array = '121.18.19.20'
        expect = 'IPv4'
        result = checkIPs(ip_array)
        self.assertEqual(result, expect)

    def testCheckIPsWhenIPv6(self):
        ip_array = '2001:0db8:0000:0000:0000:ff00:0042:8329'
        expect = 'IPv6'
        result = checkIPs(ip_array)
        self.assertEqual(result, expect)


if __name__ == '__main__':
    unittest.main()
