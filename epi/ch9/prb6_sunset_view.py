''' We are given height of buildings from east to west.
These buildings have windows facing west.
Return indices of building with sunset view.
E.g 
1) 
    East [6, 3, 7, 2, 1, 8, 9, 4] West
         [                  7, 8] 
2) 
    East [1, 10, 8, 7, 1, 4, 5, 2, 3] West
         [    2, 3, 4,       7,    9
'''

import unittest

def building_with_sunset_view(building_iter):
    '''return building id with sunset view which have windows facing west
    building_iter gives building heights from east to west
    '''
    util_stack = []
    curr_idx = 0
    while True:
        try:
            curr_building = next(building_iter)
            curr_idx += 1
            if len(util_stack) == 0:
                util_stack.append((curr_building, curr_idx))
            else:
                if curr_building >= util_stack[-1][0]:
                    while util_stack and curr_building >= util_stack[-1][0]:
                        util_stack.pop()
                util_stack.append((curr_building, curr_idx))
        except StopIteration:
            break

    return [b[1] for b in util_stack]

def building_with_sunset_view_west_to_east(building_iter):
    '''return building id with sunset view 
    building_iter gives building heightn from west to east
    '''

    result = []
    curr_idx = 0
    while True:
        try:
            curr_building = next(building_iter)
            curr_idx += 1
            if len(result) == 0:
                result.append([curr_building, curr_idx])
            else:
                if curr_building > result[-1][0]:
                    result.append([curr_building, curr_idx])
        except StopIteration:
            break
    return [curr_idx - b[1] + 1 for b in reversed(result)]


class Test_building_with_sunse(unittest.TestCase):
    def test_1(self):
        inp = [1, 10, 8, 7, 1, 4, 5, 2, 3]
        exp_out = [2, 3, 4, 7, 9]
        #east -> west
        self.assertEqual(building_with_sunset_view(iter(inp)), exp_out)

        #west -> east
        self.assertEqual(building_with_sunset_view_west_to_east(reversed(inp)), exp_out)

    def test_2(self):
        inp = [6, 3, 7, 2, 1, 8, 9, 4]
        exp_out =[7,8]
        #east -> west
        self.assertEqual(building_with_sunset_view(iter(inp)), exp_out)

        #west -> east
        self.assertEqual(building_with_sunset_view_west_to_east(reversed(inp)), exp_out)

    def test_equal_ht(self):
        inp = [5] * 1000
        exp_out =[1000]
        #east -> west
        self.assertEqual(building_with_sunset_view(iter(inp)), exp_out)

        #west -> east
        self.assertEqual(building_with_sunset_view_west_to_east(reversed(inp)), exp_out)

    def test_incr_ht(self):
        inp = range(1000)
        exp_out =[1000]
        #east -> west
        self.assertEqual(building_with_sunset_view(iter(inp)), exp_out)

        #west -> east
        self.assertEqual(building_with_sunset_view_west_to_east(reversed(inp)), exp_out)

    def test_decr_ht(self):
        inp = range(1000, 0, -1)
        exp_out = list(range(1, 1001))
        #east -> west
        self.assertEqual(building_with_sunset_view(iter(inp)), exp_out)

        #west -> east
        self.assertEqual(building_with_sunset_view_west_to_east(reversed(inp)), exp_out)

if __name__ == '__main__':
    unittest.main()





