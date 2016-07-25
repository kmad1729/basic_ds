#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> ll1;
    LinkedList<int> empty_list;

    cout << "trying to shuffle_merge 2 empty list -->";
    LinkedList<int> out_ll1;
    cout << "before ll1 -->" << endl;
    ll1.print_list();
    cout << "before empty_list -->" << endl;
    empty_list.print_list();
    out_ll1.shuffle_merge(ll1, empty_list);
    cout << "after out_ll1.shuffle_merge(ll1, empty_list) out_ll1 -->" << endl;
    out_ll1.print_list();
    cout << delim;

    ll1.push_back(5);
    cout << "trying to shuffle_merge empty and non_empty list" << endl;
    LinkedList<int> out_ll2;
    cout << "before ll1 -->" << endl;
    ll1.print_list();
    cout << "before empty_list -->" << endl;
    empty_list.print_list();
    out_ll2.shuffle_merge(ll1, empty_list);
    cout << "after out_ll2.shuffle_merge(ll1, empty_list) out_ll2 -->" << endl;
    out_ll2.print_list();
    cout << delim;

    cout << "trying to shuffle_merge non_empty and empty list" << endl;
    LinkedList<int> out_ll3;
    cout << "before ll1 -->" << endl;
    ll1.print_list();
    cout << "before empty_list -->" << endl;
    empty_list.print_list();
    out_ll3.shuffle_merge(empty_list, ll1);
    cout << "after out_ll3.shuffle_merge(empty_list, ll1) out_ll3 -->" << endl;
    out_ll3.print_list();
    cout << delim;



    LinkedList<int> ll2a;
    LinkedList<int> ll2b;
    int elems_to_insert2a[] = {5, 7, 7, 42};
    int sz_elems2a = sizeof(elems_to_insert2a) / sizeof(elems_to_insert2a[0]);
    for(int i = 0; i < sz_elems2a; i++) {
        ll2a.push_back(elems_to_insert2a[i]);
    }

    int elems_to_insert2b[] = {23, 33, 91};
    int sz_elems2b = sizeof(elems_to_insert2b) / sizeof(elems_to_insert2b[0]);
    for(int i = 0; i < sz_elems2b; i++) {
        ll2b.push_back(elems_to_insert2b[i]);
    }

    cout << "before ll2a --> " << endl;
    ll2a.print_list();
    cout << "before ll2b --> " << endl;
    ll2b.print_list();

    LinkedList<int> out_ll4;
    out_ll4.shuffle_merge(ll2a, ll2b);
    cout << "after out_ll4.shuffle_merge(ll2a, ll2b) out_ll4 -->" << endl;
    out_ll4.print_list();
    cout << delim;

    cout << "before ll2a --> " << endl;
    ll2a.print_list();

    LinkedList<int> out_ll5;
    out_ll5.shuffle_merge(ll2a, ll2a);
    cout << "after out_ll5.shuffle_merge(ll2a, ll2a) out_ll5 -->" << endl;
    out_ll5.print_list();
    cout << delim;

    cout << "before ll2a --> " << endl;
    ll2a.print_list();
    cout << "before ll1 --> " << endl;
    ll1.print_list();

    LinkedList<int> out_ll6;
    out_ll6.shuffle_merge(ll2a, ll1);
    cout << "after out_ll6.shuffle_merge(ll2a, ll1) out_ll6 -->" << endl;
    out_ll6.print_list();
    cout << delim;


}

