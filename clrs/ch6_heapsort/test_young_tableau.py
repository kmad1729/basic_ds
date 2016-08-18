'Test for young tableau questions clrs 6-3'

import unittest

from young_tableau import extract_min, LCL_INF

class Test_Young_Tableau(unittest.TestCase):
    def setUp(self):
        self.yt = \
	    [ [   2,    5,    8, LCL_INF],
	      [   3,    9,   14, LCL_INF],
	      [   4,   12,   16, LCL_INF],
	      [ LCL_INF, LCL_INF, LCL_INF, LCL_INF],
	    ] 

    def test_extract_min(self):
        min_from_yt = extract_min(self.yt)
        self.assertEqual(2, min_from_yt)
        expected_yt = \
                [ [3, 5, 8, LCL_INF],
                  [4, 9, 14, LCL_INF],
                  [12, 16, LCL_INF, LCL_INF],
	          [LCL_INF, LCL_INF, LCL_INF, LCL_INF],
                ]  
                
        self.assertEqual(expected_yt, self.yt)

        expected_yt = \
                [ [4, 5, 8, LCL_INF],
                  [9, 14, LCL_INF, LCL_INF],
                  [12, 16, LCL_INF, LCL_INF],
	          [LCL_INF, LCL_INF, LCL_INF, LCL_INF],
                ]  
        self.assertEqual(3, extract_min(self.yt))
        self.assertEqual(expected_yt, self.yt)
	


if __name__ == '__main__':
    unittest.main()
