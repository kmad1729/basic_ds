'functions to create, manipulate and work with heap data structure'


def max_heapify(lst, ind, heap_size):
    '''max_heapify a list from index ind.
    sub-trees roots at ind's children are assume to be max-heaps
    '''
    largest = ind
    left = (ind << 1) + 1
    right = (ind << 1) + 2
    if left < heap_size and lst[largest] < lst[left]:
        largest = left

    if right < heap_size and lst[largest] < lst[right]:
        largest = right

    if ind != largest:
        lst[ind], lst[largest] = lst[largest], lst[ind]
        max_heapify(lst, largest, heap_size)


