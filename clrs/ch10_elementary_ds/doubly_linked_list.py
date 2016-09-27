#!/usr/bin/env python3

from __future__ import print_function
import unittest

class DoublyLinkedList:

    def __init__(self):
        self.sentinel = {'data' : None, 'prev' : None, 'next' : None};
        self.sentinel['prev'] = self.sentinel
        self.sentinel['next'] = self.sentinel

    def insert(self, data):
        'splices an elem with data onto the front of the linked list'
        elem = {'data': data, 'next': None, 'prev': None}
        self.sentinel['next']['prev'] = elem
        elem['next'] = self.sentinel['next']
        self.sentinel['next'] = elem
        elem['prev'] = self.sentinel

    def search(self, tgt):
        'also solution to problem 10.2.4'

        self.sentinel['data'] = tgt
        x = self.sentinel['next']
        while x['data'] != tgt:
            x = x['next']
        if x == self.sentinel:
            return None
        else:
            return x

    def delete(self, data):
        ref = self.search(data)
        if ref == None:
            return None
        ref['prev']['next'] = ref['next']
        ref['next']['prev'] = ref['prev']


    def print_list(self):
        x = self.sentinel['next']
        while x != self.sentinel:
            print("{} -> ".format(x['data']), end = '' )
            x = x['next']
        print('/')


###### TESTS #####

class TestDLL(unittest.TestCase):

    def test_basic_functionality(self):
        dll = DoublyLinkedList()

        self.assertEqual(None, dll.search(23))

        dll.insert(42)
        dll.insert(45)
        dll.insert(-1)
        delim = '#' * 20

        print('dll ->')
        dll.print_list()
        print(delim)

        x = dll.search(-1)
        self.assertEqual(x['data'], -1)

if __name__ == '__main__':
    unittest.main()

