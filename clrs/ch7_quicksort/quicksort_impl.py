'implementation of quicksort from clrs textbook using partition function'

def partition(A, p, r):
    "partition arr A with bounts [p, r]. Note index 'r' is inclusive"
    assert r < len(A)
    x = A[r]
    i = p - 1

    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i + 1], A[r] = A[r], A[i + 1]
    return (i + 1)

def quicksort(A, p, r):
    "sort list A with index bounds [p, r]. Again 'r' inclusive"
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)

