#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';

    LinkedList<int> ll1;
    cout << "reverse empty list. Before ll1 ->" << endl;
    ll1.print_list();
    cout << "after ll1.reverse(). ll1 -> " << endl;
    ll1.print_list();
    cout << delim;

    ll1.push_back(5);
    cout << "reverse one elem list.Before ll1 ->" << endl;
    ll1.print_list();
    ll1.reverse();
    cout << "after ll1.reverse(). ll1 ->" << endl;
    ll1.print_list();
    cout << delim;

    ll1.push_back(23);
    cout << "reverse two elem list.Before ll1 ->" << endl;
    ll1.print_list();
    ll1.reverse();
    cout << "after ll1.reverse(). ll1 ->" << endl;
    ll1.print_list();
    cout << delim;

    ll1.push_back(25);
    cout << "reverse three elem list.Before ll1 ->" << endl;
    ll1.print_list();
    ll1.reverse();
    cout << "after ll1.reverse(). ll1 ->" << endl;
    ll1.print_list();
    cout << delim;

    LinkedList<int> ll2;
    int new_elems_to_insert2[] = {4, 9, 27, 4, 1, 3};
    int sz_new_elems2 = sizeof(new_elems_to_insert2) / sizeof(new_elems_to_insert2[0]);
    for(int i = 0; i < sz_new_elems2; i++) {
        ll2.push_back(new_elems_to_insert2[i]);
    }

    cout << "ll2 --> " << endl;
    ll2.print_list();
    ll2.reverse();    
    cout << "af ll2.reverse(). ll2 ->" << endl;
    ll2.print_list();
    cout << delim;

}

