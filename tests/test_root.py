import unittest

import server


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(server.root(), server.MESSAGE.encode("utf-8"))

    def test_something_2(self):
        self.assertNotEqual(server.root(), None)


if __name__ == '__main__':
    unittest.main()
