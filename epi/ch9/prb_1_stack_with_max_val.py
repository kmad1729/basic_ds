'''Design a stack that includes a max operation, in addition to push and pop.
The max method should return the maximum value stored in the stack
'''

from __future__ import print_function
import unittest


class Stack_MaxVal:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_item = {
                'data':item,
                'next':self.top,
                }
        if self.top is None:
            new_item['max_val'] = item
        else:
            new_item['max_val'] = max(item, self.top['max_val'])

        self.top = new_item

    def pop(self):
        if self.top is None:
            raise Exception('empty stack!')
        ret = self.top
        self.top = self.top['next']
        return ret['data']

    def maxval(self):
        if self.top is None:
            raise Exception('empty stack!')
        return self.top['max_val']
    
    def empty(self):
        return self.top is None


class Test_Stack_MaxVal(unittest.TestCase):
    def test_basic(self):
        stck = Stack_MaxVal()
        self.assertRaises(Exception, stck.pop)
        self.assertRaises(Exception, stck.maxval)
        
        lst = [(3, 3), (2, 3), (5, 5), (4, 5), (1, 5), (17, 17),
                (5, 17), (17, 17), (17, 17), (13, 17), (12, 17),
                (5, 17)]

        for i in lst:
            stck.push(i[0])

        idx = len(lst) - 1
        while not stck.empty():
            max_top = stck.maxval()
            top_val = stck.pop()
            self.assertEquals(top_val, lst[idx][0])
            self.assertEquals(max_top, lst[idx][1])

            idx -= 1


if __name__ == '__main__':
    unittest.main()
