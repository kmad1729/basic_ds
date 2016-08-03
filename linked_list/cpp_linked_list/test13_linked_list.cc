#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> ll_a;
    LinkedList<int> ll1;
    LinkedList<int> ll2;
    int new_elems_to_insert1[] = {3, 3, 3};
    int sz_new_elems1 = sizeof(new_elems_to_insert1) / sizeof(new_elems_to_insert1[0]);
    for(int i = 0; i < sz_new_elems1; i++) {
        ll1.push_back(new_elems_to_insert1[i]);
    }
    int new_elems_to_insert2[] = {3, 3};
    int sz_new_elems2 = sizeof(new_elems_to_insert2) / sizeof(new_elems_to_insert2[0]);
    for(int i = 0; i < sz_new_elems2; i++) {
        ll2.push_back(new_elems_to_insert2[i]);
    }
    cout << "ll1 --> " << endl;
    ll1.print_list();
    cout << "ll2 --> " << endl;
    ll2.print_list();
    ll_a.sorted_intersect(ll1, ll2);
    cout << "after ll_a.sorted_intersect(ll1, ll2). ll_a -->" << endl;
    ll_a.print_list();
    cout << delim;

    LinkedList<int> ll_b;
    LinkedList<int> ll3;
    LinkedList<int> ll4;
    int new_elems_to_insert3[] = {2, 5, 11, 16, 19, 19};
    int sz_new_elems3 = sizeof(new_elems_to_insert3) / sizeof(new_elems_to_insert3[0]);
    for(int i = 0; i < sz_new_elems3; i++) {
        ll3.push_back(new_elems_to_insert3[i]);
    }
    int new_elems_to_insert4[] = {5, 12, 17, 19};
    int sz_new_elems4 = sizeof(new_elems_to_insert4) / sizeof(new_elems_to_insert4[0]);
    for(int i = 0; i < sz_new_elems4; i++) {
        ll4.push_back(new_elems_to_insert4[i]);
    }
    cout << "ll3 --> " << endl;
    ll3.print_list();
    cout << "ll4 --> " << endl;
    ll4.print_list();
    ll_b.sorted_intersect(ll3, ll4);
    cout << "after ll_b.sorted_intersect(ll4, ll4). ll_b -->" << endl;
    ll_b.print_list();
    cout << delim;
}

