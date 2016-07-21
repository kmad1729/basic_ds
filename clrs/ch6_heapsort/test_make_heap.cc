#include "heap.h"
#include <iostream>
#include <iterator>

using namespace std;

int main()
{
    int arr1[] = {5, 3, 17, 10, 84, 19, 6, 22, 9};
    int arr1_sz = sizeof(arr1) / sizeof(arr1[0]);

    vector<int> A(arr1, arr1 + arr1_sz);
    cout << "before calling make_heap, A -->" << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    make_heap(A);
    cout << "after calling make_heap, A -->" << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "84 22 19 10 3 17 6 5 9 <-- expected" << endl;

    heap_sort(A);
    cout << "After calling heapsort on above vector --> " << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;
    cout << "3 5 6 9 10 17 19 22 84 <-- expected" << endl;

}
