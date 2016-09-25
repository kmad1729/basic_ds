'wap which computes the median of a stream of numbers'

from __future__ import print_function
import argparse

from heapq import heappush, heappop

class MedianMaintenance:

    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap =[]

    def insert(self, item):

        left_heap_size = len(self.left_max_heap)
        right_heap_size = len(self.right_min_heap)

        if left_heap_size == right_heap_size == 0:
            heappush(self.left_max_heap, -item)
            return

        if item < -self.left_max_heap[0]:
            heappush(self.left_max_heap, -item)
            left_heap_size += 1
        elif item > self.right_min_heap[0]:
            heappush(self.right_min_heap, item)
            right_heap_size += 1
        else:
            heappush(self.right_min_heap, item)
            right_heap_size += 1

        if abs(left_heap_size - right_heap_size) <= 1:
            return

        if left_heap_size > right_heap_size:
            i = -heappop(self.left_max_heap)
            heappush(self.right_min_heap, i)
        elif right_heap_size >left_heap_size:
            i = heappop(self.right_min_heap)
            heappush(self.left_max_heap, -i)


    def get_median(self):
        left_heap_size = len(self.left_max_heap)
        right_heap_size = len(self.right_min_heap)

        if (left_heap_size == right_heap_size):
            return -self.left_max_heap[0]
        else:
            if left_heap_size > right_heap_size:
                return -self.left_max_heap[0]
            else:
                return self.right_min_heap[0]


def get_running_median_sum_from_file(fname):
    mm = MedianMaintenance()
    result = 0
    with open(fname, 'r') as f:
        for l in f:
            mm.insert(int(l))
            result += mm.get_median()
    return result

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='compute the running median of a list of'
            ' number and find the running sum of all the medians')

    parser.add_argument('f', help='file name')
    args = parser.parse_args()

    median_sum = get_running_median_sum_from_file(args.f)
    print('sum of medians = {s}'.format(s=median_sum))
    print('sum of median mod 10000 = {m}'.format(m=(median_sum % 10000)))
