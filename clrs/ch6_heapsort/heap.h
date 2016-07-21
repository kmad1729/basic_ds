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
