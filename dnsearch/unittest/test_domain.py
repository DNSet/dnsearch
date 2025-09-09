# coding:utf-8

import unittest

from dnsearch.domain import Name


class TestName(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.name = Name("example.com")

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_magic(self):
        self.assertEqual(str(self.name), "example.com")
        self.assertEqual(len(self.name), 2)
        self.assertEqual(self.name, "example.com.")
        self.assertEqual(self.name, "example.com")
        self.assertNotEqual(self.name, "www.example.com")
        self.assertLessEqual(self.name, "www.example.com")
        self.assertLessEqual(self.name, "www.example.com")
        self.assertLess(self.name, "www.example.com")
        self.assertGreaterEqual(self.name, "com")
        self.assertGreaterEqual(self.name, "com")
        self.assertGreater(self.name, "com")

    def test_label(self):
        self.assertRaises(ValueError, Name, "a_1.com")
        self.assertRaises(ValueError, Name, "a..com")


if __name__ == "__main__":
    unittest.main()
