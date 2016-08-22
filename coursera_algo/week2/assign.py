'computing solutions to programming assignment'

from quicksort_impl import quicksort

f_name = 'inp.txt'
data = []

with open(f_name, 'r') as f:
    for l in f:
        if l.strip() != '':
            data.append(int(l))

print("length of data = {}".format(len(data)))

def default_pivot_first_elem(A, p, r):
    return p

def default_pivot_last_elem(A, p, r):
    return r

def default_pivot_median_of_3(A, p , r):
    first_elem = (A[p], p)
    last_elem = (A[r], r)
    mid_elem_ind = p + (r - p) // 2
    mid_elem = (A[mid_elem_ind], mid_elem_ind)
    return sorted([first_elem, last_elem, mid_elem])[1][1]

comps1 = quicksort(data[:], 0, len(data) - 1, default_pivot_first_elem)
comps2 = quicksort(data[:], 0, len(data) - 1, default_pivot_last_elem)
comps3 = quicksort(data[:], 0, len(data) - 1, default_pivot_median_of_3)

print("number of comparisions with first elem as pivot = {}".format(comps1))
print("number of comparisions with last elem as pivot = {}".format(comps2))
print("number of comparisions with median of 3 elem as pivot = {}".format(comps3))
