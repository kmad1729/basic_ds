#include "heap.h"
#include <iostream>
#include <iterator>

using namespace std;

int main()
{
    int arr1[] = {27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0};
    int arr1_sz = sizeof(arr1) / sizeof(arr1[0]);
    vector<int> A(arr1, arr1 + arr1_sz);

    int ind = 2;
    cout << "heap before calling max_heapify at " << ind << " on arr1 -->" << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    cout  << "after max_heapify at index " << ind << " --> " << endl;
    max_heapify(A, ind, A.size());

    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "27 17 10 16 13 9 1 5 7 12 4 8 3 0 <-- expected" << endl;
}
