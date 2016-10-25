'''We are given items 1,   2,  3,  4,  5...
with integral weights w1, w2, w3, w4, w5...
and values of items   v1, v2, v3, v4, v5...

W -> maximum weight the knapsack can carry

We would like to find what is the maximum value and what items to pack if 

Case 1) There is only 1 count of each item (art gallery)
Case 2) There is unlimited numbers of each item (supermarket)
'''

import unittest

def get_max_val(d, W):
    '''
    given data d of form
        d = {
            1 : {'weight':4, 'value':5},
            .
            .
        }

        and W (maximum knapsack capacity)
    find the maximum value of goods that can be packed
    '''
    item_weight_value_table = [ [None] * (W + 1) for i in range((len(d) + 1))]
    for item in range(len(d) + 1):
        item_weight_value_table[item][0] = 0
    for weight in range(W + 1):
        item_weight_value_table[0][weight] = 0

    for item in range(1, len(d) + 1):
        for wt in range(1, W + 1):
            if d[item]['weight'] > wt:
                item_weight_value_table[item][wt] = item_weight_value_table[item - 1][wt]
            else:
                item_weight_value_table[item][wt] = max(
                        item_weight_value_table[item - 1][wt],
                        d[item]['value'] + item_weight_value_table[item - 1][wt - d[item]['weight']])

    return item_weight_value_table[-1][-1]



class Test_knapsack_case1(unittest.TestCase):
    def setUp(self):
        self.data1 = {
                1 : {'weight': 3, 'value': 5},
                2 : {'weight': 2, 'value': 6},
                3 : {'weight': 5, 'value': 7},
                4 : {'weight': 10, 'value': 15},
                5 : {'weight': 8, 'value': 12},
                }
    def test_1(self):
        W = 1
        self.assertEqual(get_max_val(self.data1, W), 0)
        W = 2
        self.assertEqual(get_max_val(self.data1, W), 6)
        W = 3
        self.assertEqual(get_max_val(self.data1, W), 6)
        W = 5
        self.assertEqual(get_max_val(self.data1, W), 11)
        W = 8
        self.assertEqual(get_max_val(self.data1, W), 13)
        W = 10
        self.assertEqual(get_max_val(self.data1, W), 18)
        W = 11
        self.assertEqual(get_max_val(self.data1, W), 18)
        W = 12
        self.assertEqual(get_max_val(self.data1, W), 21) # items 10 + 2 -> 15 + 6
        W = 13
        self.assertEqual(get_max_val(self.data1, W), 23) # items 8 + 2 + 3 -> 12 + 6 + 5

if __name__ == '__main__':
    unittest.main()
