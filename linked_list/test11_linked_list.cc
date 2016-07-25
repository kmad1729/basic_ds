#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> lla1;
    LinkedList<int> llb1;
    LinkedList<int> ll1;;

    cout << "merging 2 empty lists --> " << endl;
    cout << "lla1 --> " << endl;
    lla1.print_list();
    cout << "llb1 --> " << endl;
    llb1.print_list();
    ll1.sorted_merge(lla1, llb1);
    cout << "after ll1.sorted_merge(lla1, llb1) ll1 --> " << endl;
    ll1.print_list();

    cout << delim;

    LinkedList<int> ll2;
    lla1.push_back(7);
    lla1.push_back(7);
    lla1.push_back(42);
    cout << "lla1 --> " << endl;
    lla1.print_list();
    cout << "llb1 --> " << endl;
    llb1.print_list();
    ll2.sorted_merge(lla1, llb1);
    cout << "after ll2.sorted_merge(lla1, llb1) ll1 --> " << endl;
    ll2.print_list();
    cout << delim;

    LinkedList<int> ll3;
    cout << "lla1 --> " << endl;
    lla1.print_list();
    cout << "llb1 --> " << endl;
    llb1.print_list();
    ll3.sorted_merge(llb1, lla1);
    cout << "after ll3.sorted_merge(llb1, lla1) ll1 --> " << endl;
    ll3.print_list();
    cout << delim;

    LinkedList<int> ll4;
    LinkedList<int> lla4;
    LinkedList<int> llb4;

    int new_elems_to_insert1[] = {5, 12, 17, 36, 84, 102};
    int sz_new_elems1 = sizeof(new_elems_to_insert1) / sizeof(new_elems_to_insert1[0]);
    for(int i = 0; i < sz_new_elems1; i++) {
        lla4.push_back(new_elems_to_insert1[i]);
    }

    int new_elems_to_insert2[] = {6, 16, 19, 24, 30, 96, 136, 154};
    int sz_new_elems2 = sizeof(new_elems_to_insert2) / sizeof(new_elems_to_insert2[0]);
    for(int i = 0; i < sz_new_elems2; i++) {
        llb4.push_back(new_elems_to_insert2[i]);
    }
    cout << "lla4 --> " << endl;
    lla4.print_list();
    cout << "llb4 --> " << endl;
    llb4.print_list();
    ll4.sorted_merge(llb4, lla4);
    cout << "after ll4.sorted_merge(llb4, lla4) ll4 --> " << endl;
    ll4.print_list();
    cout << delim;

    LinkedList<int> ll5;
    cout << "lla4 --> " << endl;
    lla4.print_list();
    cout << "llb4 --> " << endl;
    llb4.print_list();
    ll5.sorted_merge(lla4, llb4);
    cout << "after ll5.sorted_merge(lla4, llb4) ll5 --> " << endl;
    ll5.print_list();
    cout << delim;

    LinkedList<int> ll6;
    cout << "lla4 --> " << endl;
    lla4.print_list();
    ll6.sorted_merge(lla4, lla4);
    cout << "after ll6.sorted_merge(lla4, lla4) ll6 --> " << endl;
    ll6.print_list();
    cout << delim;

}


