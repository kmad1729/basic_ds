'compute the math.floor of square root of n'

import unittest
import math
import sys

def get_sqrt_math_floor(n):
    if n < 2:
        return n
    l, u = 0, n
    while l <= u:
        m = l + (u - l) // 2
        m_sqrd = m * m
        if m_sqrd <= n:
            l = m + 1
        else:
            u = m - 1
    return l - 1


class Test_GetSqrtMathFloor(unittest.TestCase):

    def test_basic_functionality(self):

        for k in range(1000, -1, -1):
            result = get_sqrt_math_floor(k)
            expected = math.floor(math.sqrt(k))
            #print("result = {} math.sqrt = {}".format(result, expected))
            self.assertEqual(result, expected)



if __name__ == '__main__':
    unittest.main()
