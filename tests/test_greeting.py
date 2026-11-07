import unittest

import greeting


class Hello(unittest.TestCase):
    def test_it_greets_by_name(self):
        self.assertEqual(greeting.hello("Ada"), "Hello, Ada!")


class Farewell(unittest.TestCase):
    def test_it_says_goodbye_by_name(self):
        self.assertEqual(greeting.farewell("Ada"), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
