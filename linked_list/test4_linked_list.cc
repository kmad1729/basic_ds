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

    cout << "after insert_sort empty ll --> " << endl;
    ll.insert_sort();
    ll.print_list();
    cout << delim;

    int elems_to_insert[] = {4, 33, 9, 12, 6, 42, 3};
    int sz_elems = sizeof(elems_to_insert) / sizeof(elems_to_insert[0]);
    int d;
    for(int i = 0; i < sz_elems; i++) {
        d = elems_to_insert[i];
        ll.push_back(d);
    }

    cout << "before insert_sort ll --> " << endl;
    ll.print_list();
    cout << delim;

    ll.insert_sort();
    cout << "after insert_sort ll --> " << endl;
    ll.print_list();
    cout << delim;

}
