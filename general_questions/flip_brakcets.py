#!/usr/bin/env python3

import unittest

'''Given the even length string of brackets. Return the flips 
needed to make the string look like a balanced bracket expression.  
You can only flip the brackets ({->} and }->{), delete or add is 
not allowed.  No additional space can be used here.
'''

def get_flip_count(s):
    result = 0
    num_open = 0

    for bracket in s:
        if bracket == '{':
            num_open += 1
        else:
            if num_open == 0:
                result += 1
                num_open += 1
            else:
                num_open -= 1

    result += (num_open // 2)
    return result

class Test_get_flip_count(unittest.TestCase):
    def test_get_flips(self):
        self.assertEqual(0, get_flip_count(''))
        self.assertEqual(0, get_flip_count('{}'))
        self.assertEqual(1, get_flip_count('}}'))
        self.assertEqual(2, get_flip_count('}}}}{}'))
        self.assertEqual(3, get_flip_count('{{{{{{'))
        self.assertEqual(4, get_flip_count('}{{{{{'))

if __name__ == '__main__':
    unittest.main()


