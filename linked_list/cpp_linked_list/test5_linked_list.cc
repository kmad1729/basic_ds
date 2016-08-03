#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    LinkedList<int> ll1;
    LinkedList<int> ll2;
    string delim = string(20, '#') + '\n';

    int elems_to_insert1[] = {7, 5, 42, 6};
    int sz_elems1 = sizeof(elems_to_insert1) / sizeof(elems_to_insert1[0]);
    int d;
    for(int i = 0; i < sz_elems1; i++) {
        d = elems_to_insert1[i];
        ll1.push_back(d);
    }

    int elems_to_insert2[] = {3, 323, 63};
    int sz_elems2 = sizeof(elems_to_insert2) / sizeof(elems_to_insert2[0]);
    for(int i = 0; i < sz_elems2; i++) {
        d = elems_to_insert2[i];
        ll2.push_back(d);
    }

    cout << delim;
    cout << "before append --> " << endl;
    cout << "ll1 -->" << endl;
    ll1.print_list();
    cout << "ll2 -->" << endl;
    ll2.print_list();
    cout << delim;
    
    ll1.append(ll2);
    cout << "after append --> " << endl;
    cout << "ll1 -->" << endl;
    ll1.print_list();
    cout << "7 -> 5 -> 42 -> 6 -> 3 -> 323 -> 63 -> / <-- expected" << endl;
    cout << "ll2 -->" << endl;
    ll2.print_list();
    cout << delim;

    LinkedList<int> empty_list;
    cout << "appending ll1 to empty_list" << endl;
    empty_list.append(ll1);
    cout << "after append --> " << endl;
    cout << "empty_list -->" << endl;
    empty_list.print_list();
    cout << "7 -> 5 -> 42 -> 6 -> 3 -> 323 -> 63 -> / <-- expected" << endl;
    cout << "ll1 -->" << endl;
    ll1.print_list();
    cout << endl;

    cout << delim;
    cout << "append an empty list to other empty list" << endl;
    LinkedList<int> el1;
    LinkedList<int> el2;
    cout << "el1 --> " << endl;
    el1.print_list();
    cout << "el2 --> " << endl;
    el2.print_list();

    el1.append(el2);
    cout << "after el1.append(el2) --> " << endl;
    cout << "el1 --> " << endl;
    el1.print_list();
    cout << "el2 --> " << endl;
    el2.print_list();
    cout << delim;

    empty_list.append(el1);
    cout << "after empty_list.append(el1) --> " << endl;
    cout << "empty_list --> " << endl;
    empty_list.print_list();
    cout << "el1 --> " << endl;
    el1.print_list();
    cout << delim;

}
