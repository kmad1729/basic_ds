#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> ll1;
    LinkedList<int> other;

    ll1.print_list();
    other.print_list();
    try {
        cout << "trying to move node from an empty list" << endl;
        ll1.move_node(other);
    } catch (domain_error e) {
        cout << "caught error: " << e.what() << endl;
    }

    cout << delim;

    other.push_back(5);
    cout << "before calling move_node --> " << endl;
    cout << "ll1 --> " << endl;
    ll1.print_list();
    cout << "other --> " << endl;
    other.print_list();

    ll1.move_node(other);
    cout << "after calling ll1.move_node(other) -->" << endl;
    cout << "ll1 --> " << endl;
    ll1.print_list();
    cout << "other --> " << endl;
    other.print_list();

    cout << delim;

    LinkedList<int> ll2;
    LinkedList<int> other2;
    int elems_to_insert2a[] = {5, 7, 7, 42};
    int sz_elems2a = sizeof(elems_to_insert2a) / sizeof(elems_to_insert2a[0]);
    for(int i = 0; i < sz_elems2a; i++) {
        ll2.push_back(elems_to_insert2a[i]);
    }

    int elems_to_insert2b[] = {23, 33, 91};
    int sz_elems2b = sizeof(elems_to_insert2b) / sizeof(elems_to_insert2b[0]);
    for(int i = 0; i < sz_elems2b; i++) {
        other2.push_back(elems_to_insert2b[i]);
    }
    cout << "before calling move_node --> " << endl;
    cout << "ll2 --> " << endl;
    ll2.print_list();
    cout << "other2 --> " << endl;
    other2.print_list();

    ll2.move_node(other2);
    cout << "after calling ll2.move_node(other) -->" << endl;
    cout << "ll2 --> " << endl;
    ll2.print_list();
    cout << "other2 --> " << endl;
    other2.print_list();
    cout << delim;

}

