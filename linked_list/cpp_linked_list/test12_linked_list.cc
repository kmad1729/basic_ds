#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> ll1;

    cout << "merge_sort on empty list -->" << endl;
    cout << "ll1 --> " << endl;
    ll1.print_list();
    ll1.merge_sort();
    cout << "after ll1.merge_sort() ll1 -> " << endl;
    ll1.print_list();

    cout << delim;

    ll1.push_back(32);
    cout << "merge_sort on single elem list -->" << endl;
    cout << "ll1 --> " << endl;
    ll1.print_list();
    ll1.merge_sort();
    cout << "after ll1.merge_sort() ll1 -> " << endl;
    ll1.print_list();
    cout << delim;

    LinkedList<int> ll2;
    ll2.push_back(32);
    ll2.push_back(3);
    cout << "merge_sort on double elem list -->" << endl;
    cout << "ll2 --> " << endl;
    ll2.print_list();
    ll2.merge_sort();
    cout << "after ll2.merge_sort() ll2 -> " << endl;
    ll2.print_list();
    cout << delim;

    LinkedList<int> ll3;
    int new_elems_to_insert[] = {5, 7, 42, 12, 6, 18, 96, 3, 4};
    int sz_new_elems = sizeof(new_elems_to_insert) / sizeof(new_elems_to_insert[0]);
    for(int i = 0; i < sz_new_elems; i++) {
        ll3.push_back(new_elems_to_insert[i]);
    }
    cout << "merge_sort on list -->" << endl;
    cout << "ll3 --> " << endl;
    ll3.print_list();
    ll3.merge_sort();
    cout << "after ll3.merge_sort() ll3 -> " << endl;
    ll3.print_list();
    cout << delim;
}

