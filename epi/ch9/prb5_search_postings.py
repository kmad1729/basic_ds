'''postings list is singly-linked list with an additional jump field at each node
write recursive and iterative routines that compute the jump-first order.
assume that each node has an integer-valued field that holds the order, and is 
initialized to -1.
'''

import unittest

def calc_jump_first_helper(n, order):
    if n != None and n['order'] == -1:
        n['order'] = order[0]
        order[0] += 1
        calc_jump_first_helper(n['jump'], order)
        calc_jump_first_helper(n['next'], order)

def calc_jump_first_order_recur(n):
    curr_order = [0]
    calc_jump_first_helper(n, curr_order)

class Test_jump_order(unittest.TestCase):

    def test_1(self):
        a_node = {'order': -1}
        b_node = {'order': -1}
        c_node = {'order': -1}
        d_node = {'order': -1}
        e_node = {'order': -1}
        f_node = {'order': -1}

        a_node['next'] = b_node
        b_node['next'] = c_node
        c_node['next'] = d_node
        d_node['next'] = e_node
        e_node['next'] = f_node
        f_node['next'] = None

        a_node['jump'] = c_node
        b_node['jump'] = b_node
        c_node['jump'] = b_node
        d_node['jump'] = c_node
        e_node['jump'] = f_node
        f_node['jump'] = f_node

        head = a_node

        calc_jump_first_order_recur(head)

        self.assertEqual(a_node['order'], 0)
        self.assertEqual(b_node['order'], 2)
        self.assertEqual(c_node['order'], 1)
        self.assertEqual(d_node['order'], 3)
        self.assertEqual(e_node['order'], 4)
        self.assertEqual(f_node['order'], 5)

    def test_2(self):
        a_node = {'order': -1}
        b_node = {'order': -1}
        c_node = {'order': -1}
        d_node = {'order': -1}
        e_node = {'order': -1}

        a_node['jump'] = e_node
        b_node['jump'] = b_node
        c_node['jump'] = e_node
        d_node['jump'] = c_node
        e_node['jump'] = e_node

        a_node['next'] = b_node
        b_node['next'] = c_node
        c_node['next'] = d_node
        d_node['next'] = e_node
        e_node['next'] = None


        head = a_node

        calc_jump_first_order_recur(head)

        self.assertEqual(a_node['order'], 0)
        self.assertEqual(b_node['order'], 2)
        self.assertEqual(c_node['order'], 3)
        self.assertEqual(d_node['order'], 4)
        self.assertEqual(e_node['order'], 1)
                
    def test_3(self):
        a_node = {'order': -1}
        b_node = {'order': -1}
        c_node = {'order': -1}
        d_node = {'order': -1}

        a_node['jump'] = c_node
        b_node['jump'] = d_node
        c_node['jump'] = b_node
        d_node['jump'] = d_node

        a_node['next'] = b_node
        b_node['next'] = c_node
        c_node['next'] = d_node
        d_node['next'] = None


        head = a_node

        calc_jump_first_order_recur(head)

        self.assertEqual(a_node['order'], 0)
        self.assertEqual(b_node['order'], 2)
        self.assertEqual(c_node['order'], 1)
        self.assertEqual(d_node['order'], 3)

if __name__ == '__main__':
    unittest.main()
