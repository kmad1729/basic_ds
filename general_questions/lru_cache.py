'''Question: Implement a Least Recently Used (LRU) cache for a given cache size.
'''

import unittest


class LRU:
    def __init__(self, lru_size):
        self.sz = lru_size
        self.sentinel = {}
        self.sentinel['prev'] = self.sentinel
        self.sentinel['next'] = self.sentinel

        self.data = {}

    def set(self, key, value):
        k = key
        v = value

        if k in self.data:
            k_node = self.data[k]
            del self.data[k]
            k_node['next']['prev'] = k_node['prev']
            k_node['prev']['next'] = k_node['next']

        if len(self.data) >= self.sz:
            #need to evict the last node
            last_node = self.sentinel['prev']
            last_node['prev']['next'] = last_node['next']
            last_node['next']['prev'] = last_node['prev']
            del self.data[last_node['data'][0]]

        new_node = {'data': (k, v)}
        self.data[k] = new_node
        new_node['next'] = self.sentinel['next']
        new_node['prev'] = self.sentinel
        self.sentinel['next']['prev'] = new_node
        self.sentinel['next'] = new_node

    def get(self, key):
        k = key
        if k not in self.data:
            return -1

        #move k to the front of the list
        k_node = self.data[k]

        #delete k_node
        k_node['prev']['next'] = k_node['next']
        k_node['next']['prev'] = k_node['prev']

        #move k_node to the front
        k_node['next'] = self.sentinel['next']
        k_node['prev'] = self.sentinel
        self.sentinel['next']['prev'] = k_node
        self.sentinel['next'] = k_node

        return k_node['data'][1]

    def get_lru(self):
        c_n = self.sentinel['prev']
        result = []
        while c_n != self.sentinel:
            result.append(c_n['data'][0])
            c_n = c_n['prev']
        return result




class Test_LRU(unittest.TestCase):
    def test_1(self):
        inp_size = 5 
        cache = LRU(inp_size)
        self.assertEqual([], cache.get_lru())
        cache.set('A', 'Apple')
        cache.set('B', 'Ball')
        cache.set('C', 'Cat')

        self.assertEqual(['A', 'B', 'C'], cache.get_lru())
        cache.set('D', 'Dog')
        cache.set('E', 'Elephant')
        self.assertEqual(['A', 'B', 'C', 'D', 'E'], cache.get_lru())

        self.assertEqual('Apple', cache.get('A'))
        cache.set('F', 'Frog')
        self.assertEqual(['C', 'D', 'E', 'A', 'F'], cache.get_lru())

        cache.set('B', 'Ball')
        self.assertEqual(['D', 'E', 'A', 'F', 'B'], cache.get_lru())
        self.assertEqual('Elephant', cache.get('E'))

        self.assertEqual(['D', 'A', 'F', 'B', 'E'], cache.get_lru())

        cache.set('B', "Basket")
        self.assertEqual('Frog', cache.get('F'))
        self.assertEqual('Basket', cache.get('B'))
        self.assertEqual('Dog', cache.get('D'))
        print(cache.get_lru())


if __name__ == '__main__':
    unittest.main()

    '''
    10,[set(10,13),set(3,17),set(6,11),set(10,5),set(9,10),get(13),set(2,19),get(2),get(3),set(5,25),get(8),set(9,22),set(5,5),set(1,30),get(11),set(9,12),get(7),get(5),get(8),get(9),set(4,30),set(9,3),get(9),get(10),get(10),set(6,14),set(3,1),get(3),set(10,11),get(8),set(2,14),get(1),get(5),get(4),set(11,4),set(12,24),set(5,18),get(13),set(7,23),get(8),get(12),set(3,27),set(2,12),get(5),set(2,9),set(13,4),set(8,18),set(1,7),get(6),set(9,29),set(8,21),get(5),set(6,30),set(1,12),get(10),set(4,15),set(7,22),set(11,26),set(8,17),set(9,29),get(5),set(3,4),set(11,30),get(12),set(4,29),get(3),get(9),get(6),set(3,4),get(1),get(10),set(3,29),set(10,28),set(1,20),set(11,13),get(3),set(3,12),set(3,8),set(10,9),set(3,26),get(8),get(7),get(5),set(13,17),set(2,27),set(11,15),get(12),set(9,19),set(2,15),set(3,16),get(1),set(12,17),set(9,1),set(6,19),get(4),get(5),get(5),set(8,1),set(11,7),set(5,2),set(9,28),get(1),set(2,2),set(7,4),set(4,22),set(7,24),set(9,26),set(13,28),set(11,26)]
    '''
