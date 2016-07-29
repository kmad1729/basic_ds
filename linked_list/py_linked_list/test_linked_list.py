#!/usr/bin/env python3

from linked_list import build123, LinkedList_Node

import unittest

class TestLinkedList(unittest.TestCase):

    def test_build123(self):
        l1 = build123()
        l1.print()
        

if __name__ == '__main__':
    unittest.main()
