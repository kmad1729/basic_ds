#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    LinkedList<int> ll;
    string delim = string(20, '#') + '\n';
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;

    int elems_to_insert[] = {7, 5, 42, 6, 5, 5, 6, -1};
    int sz_elems = sizeof(elems_to_insert) / sizeof(elems_to_insert[0]);
    int d;
    for(int i = 0; i < sz_elems; i++) {
        d = elems_to_insert[i];

        cout << "inserting " << d << " in ll " << endl;
        ll.sorted_insert(d);
        cout << "ll -> " << endl;
        ll.print_list();
        cout << delim;
    }


}
