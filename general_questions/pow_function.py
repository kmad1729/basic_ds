'implement a pow function pow(base, exponent)'

from math import pow
import unittest

def my_pow(base, exponent):
    pass


class Test_my_pow(unittest.TestCase):

    def test_positive_exp(self):
        tests = [ (3, 5),
                    (3, 6),
                    (3, 15),
                ]
        for b, p in tests:
            self.assertEquals(my_pow(b, p), pow(b, p))

if __name__ == '__main__':
    unittest.main()
