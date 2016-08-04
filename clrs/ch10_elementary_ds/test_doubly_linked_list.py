#!/usr/bin/env python3

import unittest

from doubly_linked_list import DoublyLinkedList

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

