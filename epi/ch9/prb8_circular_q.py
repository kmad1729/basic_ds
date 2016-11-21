'implement a circular q using an array'


class MyQueue:
    def __init__(self, max_capacity):
        self.util_arr = [None] * (max_capacity + 1)
        self.scale_factor = 2
        self.head_idx = 0
        self.tail_idx = 0

    def is_q_full(self):
        if self.tail_idx == len(self.util_arr) - 1:
            return self.head_idx == 0
        else:
            return self.tail_idx + 1 == self.head_idx

    def is_q_empty(self):
        return self.head_idx == self.tail_idx

    def enqueue(self, item):
        if self.is_q_full():
            self._resize()
        self.util_arr[self.tail_idx] = item
        if self.tail_idx == len(self.util_arr) - 1:
            self.tail_idx = 0
        else:
            self.tail_idx += 1

    def dequeue(self):
        if self.is_q_empty():
            raise Exception("Cannot dequeue from empty q")
        ret = self.util_arr[self.head_idx]
        if self.head_idx == len(self.util_arr) - 1:
            self.head_idx = 0
        else:
            self.head_idx += 1
        return ret

    def _resize(self):
        new_arr = [None] * (1 + (self.scale_factor * (len(self.util_arr) - 1)))
        counter = 0
        for i in range(self.head_idx, len(self.util_arr) - 1):
            new_arr[counter] = self.util_arr[i]
            counter += 1
        if self.tail_idx < self.head_idx:
            new_arr[counter] = self.util_arr[-1]
            counter += 1
            for i in range(self.tail_idx):
                new_arr[counter] = self.util_arr[i]
                counter += 1
        self.util_arr = new_arr
        self.head_idx = 0
        self.tail_idx = counter


import unittest

class Test_Circular_Q(unittest.TestCase):
    def test_1(self):
        q = MyQueue(max_capacity=1)
        self.assertRaises(Exception, q.dequeue)

        q.enqueue(5)
        self.assertTrue(q.is_q_full())

        q.enqueue(6)
        self.assertEqual(3, len(q.util_arr))

        self.assertEqual(5, q.dequeue())
        self.assertEqual(3, len(q.util_arr))
        
        self.assertEqual(6, q.dequeue())
        self.assertEqual(3, len(q.util_arr))
        self.assertRaises(Exception, q.dequeue)

        q.enqueue(7)
        q.enqueue(8)
        q.enqueue(9)
        q.enqueue(10)
        self.assertEqual(5, len(q.util_arr))
        self.assertTrue(q.is_q_full())

if __name__ == '__main__':
    unittest.main()
