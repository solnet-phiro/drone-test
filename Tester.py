__author__ = 'pr1438'

import unittest

class Tester (unittest.TestCase):
    def testAdd(self):
        self.assertEqual(7,7,"Not equal")

    def testAdd2(self):
        self.assertEqual(9,9,"Not equal")