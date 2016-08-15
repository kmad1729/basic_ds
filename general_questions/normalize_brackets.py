#!/usr/bin/env python3
'''given a list of nested empty lists remove the nestedness and return
single elem lists
e.g. [[]] -> []
[ [[[]]], []] -> [[], []]
[ [], [[]], [[[]]]] -> [[], [], []]
[[ [[[]]], [], [[]]  ]] -> [[], [], []]
'''
import unittest

def normalize_brackets(lst):
    if len(lst) == 1:
        lst = normalize_brackets(lst[0])
    else:
        for i, l in enumerate(lst):
            lst[i] = normalize_brackets(lst[i])

    return lst


class Test_normalize_brackets(unittest.TestCase):
    def test_basic_functionality(self):
        l = [[ [[[]]], [], [[]]  ]]  
        l = normalize_brackets(l)
        self.assertEqual(l, [[], [], []])

if __name__ == '__main__':
    unittest.main()




