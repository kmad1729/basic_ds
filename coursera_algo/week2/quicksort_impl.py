'quicksort implementation from the class.'

def quicksort(A, p, r, default_pivot_ind = (lambda arr, b, e: b)):
    '''implementation of quicksort. Sort an array A[p...r] p and r inclusive.
    Pivot is always the 1st elem of the array.  Returns the number of comparisons.
    get_default_pivot_fun functionis returns the default pivot index for array A from [p..r]
    '''

    if p >= r:
        return 0


    pivot_ind = partition(A, p, r, default_pivot_ind)
    left_comparisons = quicksort(A, p, pivot_ind - 1, default_pivot_ind)
    right_comparisons = quicksort(A, pivot_ind + 1, r, default_pivot_ind)
    return (r - p + left_comparisons + right_comparisons)

def partition(A, l, r, default_pivot_ind):
    '''Partitions array A with pivot at index 0. Returns the 0-based index of pivot in a 
    sorted array.
    '''

    pivot_ind = default_pivot_ind(A, l, r)
    A[l], A[pivot_ind] = A[pivot_ind], A[l]
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[i - 1], A[l] = A[l], A[i - 1]
    return i - 1




