'''Coumpue the max weighted independent set for a given path graph
Definitions:
    path graph: a graph (V, E) where vertices are in a single path
    e.g 1 -> 2 -> 3 -> 4 -> 5
    indpendent set of a graph: a set S of vertices where no 2 vertices have 
        a common edge
    max weight: sum of weights is maximum


E.g: for weights [5, 1, 4, 3, 6, 8] i.e 
    vertex 1 has weight 5
    vertex 2 has weight 1
    vertex 3 has weight 4 and so on..

    max weight independent set is {1, 3, 6} with weight 17

    for weights [5, 1, 4, 3, 9, 8] -> {1, 3, 5} with weight 18
'''


import unittest

def get_max_wt_ind_set(weights):
    util_arr = [0] + weights

    for i in range(2, len(util_arr)):
        util_arr[i] = max(util_arr[i - 1], weights[i - 1] + util_arr[i - 2])

    result_set = set()
    i = len(util_arr) - 1
    while i > 0:
        if util_arr[i - 1] >= util_arr[i - 2] + weights[i - 1]:
            i -= 1
        else:
            result_set.add(i)
            i -= 2
    return result_set



class Test_max_weight_ind_set(unittest.TestCase):

    def test_1(self):
        inp_wts = [5, 1, 4, 3, 6, 8]
        self.assertEqual({1, 3, 6}, get_max_wt_ind_set(inp_wts))

    def test_2(self):
        inp_wts = [5, 1, 4, 3, 6, 8]
        self.assertEqual({1, 3, 6}, get_max_wt_ind_set(inp_wts))

    def test_3(self):
        inp_wts = [1, 4, 5, 4]
        self.assertEqual({2, 4}, get_max_wt_ind_set(inp_wts))


if __name__ == '__main__':
    unittest.main()
