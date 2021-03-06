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

def build_max_heap(lst):
    heap_size = len(lst)
    for i in range( (heap_size - 1) // 2, -1, -1):
        max_heapify(lst, i, heap_size)

def heap_sort(lst):
    build_max_heap(lst)
    heap_size = len(lst)
    for i in range(heap_size - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heap_size -= 1
        max_heapify(lst, 0, heap_size)

#priority queue related methods
def heap_max(lst):
    return lst[0]

def heap_extract_max(lst):
    assert(len(lst)) > 0
    lst[0], lst[-1] = lst[-1], lst[0]
    result = lst.pop()
    max_heapify(lst, 0, len(lst))
    return result

def _parent(i):
    return (i - 1) >> 1

def heap_increase_key(lst, ind, key):
    assert 0 <= ind < len(lst)
    if key <= lst[ind]:
        raise Exception(
                "current key value at {i} is already {l_i} which is >= {key}".format(
                    i = ind, l_i = lst[ind], key = key))
    lst[ind] = key
    while ind > 0 and lst[_parent(ind)] < lst[ind]:
        lst[_parent(ind)], lst[ind] = lst[ind], lst[_parent(ind)]
        ind = _parent(ind)


def max_heap_insert(lst, key, lst_range_min):
    lst.append(lst_range_min)
    heap_increase_key(lst, len(lst) - 1, key)
