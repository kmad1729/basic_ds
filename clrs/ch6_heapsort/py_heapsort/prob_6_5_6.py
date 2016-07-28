'implement first-in first-out queue using a priority queue'

from heap import max_heap_insert, heap_extract_max, heap_max

class Queue_PQ:
    
    def __init__(self):
        self._pq = []
        self._last_ind = 0
        self.lst_range_min = (float('-inf'), float('-inf'))

    def enqueue(self, elem):
        max_heap_insert(self._pq, (self._last_ind, elem), self.lst_range_min)
        self._last_ind -= 1

    def dequeue(self):
        if len(self._pq) == 0:
            raise Exception('cannot dequeue empty queue')
        return heap_extract_max(self._pq)[1]

    def empty(self):
        return len(self._pq) == 0

    def front(self):
        return heap_max(self._pq)[1]

    def __repr__(self):
        return str(list(map(lambda x: x[1], self._pq)))

    def __len__(self):
        return len(self._pq)

