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

    int new_elems_to_insert1[] = {4, 9, 27, 4, 1, 3};
    int sz_new_elems1 = sizeof(new_elems_to_insert1) / sizeof(new_elems_to_insert1[0]);
    for(int i = 0; i < sz_new_elems1; i++) {
        ll1.push_back(new_elems_to_insert1[i]);
    }

    cout << "ll1 --> " << endl;
    ll1.print_list();
    ll1.reverse();    
    cout << "af ll1.reverse(). ll1 ->" << endl;
    ll1.print_list();
    cout << delim;
}

