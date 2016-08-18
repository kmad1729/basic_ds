#include "heap.h"
#include <iostream>
#include <iterator>

using namespace std;

int main()
{
    int arr1[] = {5, 13, 2, 25, 7, 17, 20, 8, 4};
    int arr1_sz = sizeof(arr1) / sizeof(arr1[0]);

    vector<int> A(arr1, arr1 + arr1_sz);

    cout << "before calling heap_sort. A --> " << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    heap_sort(A);
    cout << "after calling heap_sort. A --> " << endl;
    copy(A.begin(), A.end(), ostream_iterator<int>(cout, " "));
    cout << endl;

    cout << "2 4 5 7 8 13 17 20 25 <-- expected" << endl;
}
