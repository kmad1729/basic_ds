#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> ll1;

    cout << "ll1 -> " << endl;
    ll1.print_list();
    ll1.remove_duplicates();
    cout << "removing duplicates from empty list. ll1 -->" << endl;
    ll1.print_list();
    cout << delim;

    int d;
    int elems_to_insert1[] = {5, 7, 7, 42, 42, 42, 47, 49, 49};
    int sz_elems1 = sizeof(elems_to_insert1) / sizeof(elems_to_insert1[0]);
    for(int i = 0; i < sz_elems1; i++) {
        d = elems_to_insert1[i];
        ll1.push_back(d);
    }

    cout << "ll1 -> " << endl;
    ll1.print_list();
    ll1.remove_duplicates();
    cout << "after removing duplicates from the list. ll1 -->" << endl;
    ll1.print_list();
    cout << delim;

    LinkedList<int> ll2;
    int elems_to_insert2[] = {7, 7, 7, 7};
    int sz_elems2 = sizeof(elems_to_insert2) / sizeof(elems_to_insert2[0]);
    for(int i = 0; i < sz_elems2; i++) {
        d = elems_to_insert2[i];
        ll2.push_back(d);
    }
    cout << "ll2 -> " << endl;
    ll2.print_list();
    ll2.remove_duplicates();
    cout << "after removing duplicates from  list. ll2 -->" << endl;
    ll2.print_list();
    cout << delim;

    LinkedList<int> ll3;
    int elems_to_insert3[] = {7, 7, 7};
    int sz_elems3 = sizeof(elems_to_insert3) / sizeof(elems_to_insert3[0]);
    for(int i = 0; i < sz_elems3; i++) {
        d = elems_to_insert3[i];
        ll3.push_back(d);
    }
    cout << "ll3 -> " << endl;
    ll3.print_list();
    ll3.remove_duplicates();
    cout << "after removing duplicates from  list. ll3 -->" << endl;
    ll3.print_list();
    cout << delim;

    LinkedList<int> ll4;
    int elems_to_insert4[] = {48};
    int sz_elems4 = sizeof(elems_to_insert4) / sizeof(elems_to_insert4[0]);
    for(int i = 0; i < sz_elems4; i++) {
        d = elems_to_insert4[i];
        ll4.push_back(d);
    }
    cout << "ll4 -> " << endl;
    ll4.print_list();
    ll4.remove_duplicates();
    cout << "after removing duplicates from  list. ll4 -->" << endl;
    ll4.print_list();
    cout << delim;

}
