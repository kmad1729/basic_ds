"find the i'th order statistic in an array A"

from random import randint

def randomized_partition(A, start_ind, end_ind):
    'partition array A randomly by choosing a random pivot'
    piv_ind = randint(start_ind, end_ind)
    A[start_ind], A[piv_ind] = A[piv_ind], A[start_ind]
    i = start_ind + 1
    pivot = A[start_ind]

    for j in range(start_ind + 1, end_ind + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1

    A[start_ind], A[i - 1] = A[i - 1], A[start_ind]
    return i - 1


def random_select(A, start_ind, end_ind, i_order_to_find):
    'find the ith order statistic from array A'

    if start_ind == end_ind:
        return A[start_ind]

    j = randomized_partition(A, start_ind, end_ind)
    k = j - start_ind

    if k + 1 == i_order_to_find:
        return A[j]
    elif k + 1 > i_order_to_find:
        return random_select(A, start_ind, j - 1, i_order_to_find)
    else:
        return random_select(A, j + 1, end_ind, i_order_to_find -k -1)

