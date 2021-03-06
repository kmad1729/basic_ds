#pragma once
#include <vector>
#include <algorithm>

using std::vector;

void max_heapify(vector<int>& A, int index, int heap_size)
{
    int left = (index << 1) + 1;
    int right = (index << 1) + 2;
    int largest = index;
    if(left < heap_size && A[left] > A[largest])
        largest = left;
    if(right < heap_size && A[right] > A[largest])
        largest = right;
    if(largest != index) {
        std::swap(A[index], A[largest]);
        max_heapify(A, largest, heap_size);
    }
}

void make_heap(vector<int>& A)
{
    int heap_size = A.size();
    for(int i = heap_size / 2; i >= 0; i--) {
        max_heapify(A, i, heap_size);
    }
}

void heap_sort(vector<int>& A)
{
    int heap_size = A.size();
    make_heap(A);
    for(int i = heap_size - 1; i > 0; i--) {
        std::swap(A[i], A[0]);
        heap_size--;
        max_heapify(A, 0, heap_size);
    }
}
