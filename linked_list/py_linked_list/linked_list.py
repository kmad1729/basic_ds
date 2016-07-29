#!/usr/bin/env python3

class LinkedList_Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def print(self):
        while self != None:
            print(self.data, end = "->")
        print("/")


def build123():
    ll_head = LinkedList_Node(1)
    ll_head.next = LinkedList_Node(2)
    ll_head.next.next = LinkedList_Node(3)
    return ll_head
