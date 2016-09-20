import unittest

from compute_scc import DFS_loop, get_G_rev

class Test_DFS_loop(unittest.TestCase):
    
    def setUp(self):
        self.G = {
                1 : [4],
                4 : [7],
                7 : [1],
                9 : [3, 7],
                6 : [9],
                3 : [6],
                8 : [5, 6],
                2 : [8],
                5 : [2],
                }

        self.G_rev = {
                1 : [7],
                4 : [1],
                7 : [4, 9],
                9 : [6],
                6 : [3, 8],
                3 : [9],
                8 : [2],
                2 : [5],
                5 : [8],
                }

    def test_dfs_loop(self):
        num_nodes = len(self.G_rev)
        finish_times = [1e9] * (num_nodes + 1)
        DFS_loop(self.G_rev, finish_times)
        for i, t in enumerate(finish_times[1:], 1):
            print("{i} finished at {t}".format(i=i,t=t))

        expected_finish_times = [7, 3, 1, 8, 2, 5, 9, 4, 6 ]

        self.assertEquals(expected_finish_times, finish_times[1:])

    def test_get_G_rev(self):
        computed_rev = get_G_rev(self.G)
        self.assertEquals(computed_rev, self.G_rev)


if __name__ == '__main__':
    unittest.main()
