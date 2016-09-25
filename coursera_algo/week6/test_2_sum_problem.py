import unittest

from two_sum_problem import check_sum_exists, count_tgt_sums_for_range, \
       check_sums_in_sorted_list

class Test_2_sum_prob(unittest.TestCase):

    def setUp(self):
        self.s = {1, -1, 2, 4, 3, 0}

    def test_sum_exists(self):
        tgt_sums = {
                -2:False,
                -1:True,
                0:True,
                1:True,
                2:True,
                3:True,
                6:True,
                5:True,
                7:True,
                8:False,
                }

        for t, exists in tgt_sums.items():
            if exists:
                self.assertTrue(check_sum_exists(self.s, t))
            else:
                self.assertFalse(check_sum_exists(self.s, t))
    def test_count_tgt_sums(self):
        self.assertEquals(0, count_tgt_sums_for_range(self.s, -2, -2))
        self.assertEquals(1, count_tgt_sums_for_range(self.s, 0, 0))
        self.assertEquals(2, count_tgt_sums_for_range(self.s, 0, 1))
        self.assertEquals(2, count_tgt_sums_for_range(self.s, 0, 1))
        self.assertEquals(9, count_tgt_sums_for_range(self.s, -1, 8))
        self.assertEquals(9, count_tgt_sums_for_range(self.s, -1, 9))

    def test_count_sum_in_sorted_list(self):
        self.assertEquals(0, check_sums_in_sorted_list(self.s, -2, -2))
        self.assertEquals(1, check_sums_in_sorted_list(self.s, 0, 0))
        self.assertEquals(2, check_sums_in_sorted_list(self.s, 0, 1))
        self.assertEquals(2, check_sums_in_sorted_list(self.s, 0, 1))
        self.assertEquals(9, check_sums_in_sorted_list(self.s, -1, 8))
        self.assertEquals(9, check_sums_in_sorted_list(self.s, -1, 9))

if __name__ == '__main__':
    unittest.main()
