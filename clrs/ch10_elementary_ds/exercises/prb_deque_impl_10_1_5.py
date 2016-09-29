import unittest


class Clrs_Deque:
    '''deque implementation. Supports append_right, append_left, pop_right, pop_left in O(1) time
    '''

    def __init__(self, max_sz = 100):
        self.q_sz = max_sz + 1
        self.util_arr = [None] * self.q_sz
        self.head_ptr = 0
        self.tail_ptr = 0

    def _is_empty(self):
        return self.head_ptr == self.tail_ptr

    def _is_full(self):
        if self.tail_ptr == self.q_sz - 1:
            return self.head_ptr == 0
        else:
            return self.tail_ptr + 1 == self.head_ptr

    def append_left(self, item):
        if self._is_full():
            raise Exception('Overflow!')

        if self.head_ptr == 0:
            self.head_ptr = self.q_sz - 1
        else:
            self.head_ptr -= 1

        self.util_arr[self.head_ptr] = item

    def append_right(self, item):
        if self._is_full():
            raise Exception('Overflow!')

        self.util_arr[self.tail_ptr] = item
        if self.tail_ptr == self.q_sz - 1:
            self.tail_ptr = 0
        else:
            self.tail_ptr += 1

    def pop_left(self):
        if self._is_empty():
            raise Exception('Underflow')
        x = self.util_arr[self.head_ptr]
        if self.head_ptr == self.q_sz - 1:
            self.head_ptr = 0
        else:
            self.head_ptr += 1

        return x

    def pop_right(self):
        if self._is_empty():
            raise Exception('Underflow')

        if self.tail_ptr == 0:
            self.tail_ptr = self.q_sz - 1
        else:
            self.tail_ptr -= 1

        return self.util_arr[self.tail_ptr]


#TEST CASES

class Test_Deque_Impl(unittest.TestCase):
    def test_basic_functionality(self):
        dq = Clrs_Deque(3)

        self.assertRaises(Exception, dq.pop_right)
        self.assertRaises(Exception, dq.pop_left)

        dq.append_right(5)
        self.assertEquals([5, None, None, None], dq.util_arr)

        dq.append_left(6)
        self.assertEquals([5, None, None, 6], dq.util_arr)

        dq.append_right(7)
        self.assertEquals([5, 7, None, 6], dq.util_arr)

        self.assertRaises(Exception, dq.append_left, 16)
        self.assertRaises(Exception, dq.append_right, 16)

        self.assertEquals(3, dq.head_ptr)
        self.assertEquals(6, dq.pop_left())
        self.assertEquals(0, dq.head_ptr)

        self.assertEquals(5, dq.pop_left())

        self.assertEquals(7, dq.pop_right())

        self.assertRaises(Exception, dq.pop_right)
        self.assertRaises(Exception, dq.pop_left)

        dq.append_left(8)
        dq.append_left(16)
        dq.append_left(4)
        #4 <-> 16 <-> 8 

        self.assertRaises(Exception, dq.append_left, 42)
        self.assertRaises(Exception, dq.append_right, 42)

        self.assertEquals(8, dq.pop_right())
        self.assertEquals(16, dq.pop_right())
        self.assertEquals(4, dq.pop_right())

        self.assertRaises(Exception, dq.pop_right)
        self.assertRaises(Exception, dq.pop_left)


if __name__ == '__main__':
    unittest.main()
            





