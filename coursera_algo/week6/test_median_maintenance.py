import unittest
from median_maintenance import MedianMaintenance

class Test_median_maintenance(unittest.TestCase):

    def test_insert(self):

        l1 = [6, 4, 2, 3, 1, 5, -1, 0, 43]

        i1 = iter(l1)

        mm = MedianMaintenance()

        #inserting 6
        mm.insert(next(i1))
        self.assertEquals(6, mm.get_median())
        self.assertEquals(1, len(mm.left_max_heap))
        self.assertEquals(0, len(mm.right_min_heap))

        #inserting 4
        mm.insert(next(i1))
        self.assertEquals(4, mm.get_median())
        self.assertEquals(1, len(mm.left_max_heap))
        self.assertEquals(1, len(mm.right_min_heap))

        #inserting 2
        mm.insert(next(i1))
        self.assertEquals(4, mm.get_median())
        self.assertEquals(2, len(mm.left_max_heap))
        self.assertEquals(1, len(mm.right_min_heap))

        #inserting 3
        mm.insert(next(i1))
        self.assertEquals(3, mm.get_median())
        self.assertEquals(2, len(mm.left_max_heap))
        self.assertEquals(2, len(mm.right_min_heap))

        #inserting 1
        mm.insert(next(i1))
        self.assertEquals(3, mm.get_median())
        self.assertEquals(3, len(mm.left_max_heap))
        self.assertEquals(2, len(mm.right_min_heap))

        #inserting 5
        mm.insert(next(i1))
        self.assertEquals(3, mm.get_median())
        self.assertEquals(3, len(mm.left_max_heap))
        self.assertEquals(3, len(mm.right_min_heap))

        #inserting -1
        mm.insert(next(i1))
        self.assertEquals(3, mm.get_median())
        self.assertEquals(4, len(mm.left_max_heap))
        self.assertEquals(3, len(mm.right_min_heap))

        #inserting 0
        mm.insert(next(i1))
        self.assertEquals(2, mm.get_median())
        self.assertEquals(4, len(mm.left_max_heap))
        self.assertEquals(4, len(mm.right_min_heap))

        #inserting 42
        mm.insert(next(i1))
        self.assertEquals(3, mm.get_median())
        self.assertEquals(4, len(mm.left_max_heap))
        self.assertEquals(5, len(mm.right_min_heap))

if __name__ == '__main__':
    unittest.main()
