#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    string delim = string(20, '#') + '\n';
    LinkedList<int> lla1;
    LinkedList<int> llb1;
    LinkedList<int> empty_list;

    cout << "alternating_split of empty list --> " << endl;
    empty_list.alternating_split(lla1, llb1);
    cout << "after empty_list.alternating_split(lla1, llb1) -->" << endl;
    cout << "lla1 --> " << endl;
    lla1.print_list();
    cout << "llb1 --> " << endl;
    llb1.print_list();
    cout << delim;

    LinkedList<int> new_list;
    LinkedList<int> out_list_a;
    LinkedList<int> out_list_b;
    int new_elems_to_insert[] = {5, 7, 8, 3, 11, 93, 34, 32, 7, 42};
    int sz_new_elems = sizeof(new_elems_to_insert) / sizeof(new_elems_to_insert[0]);
    for(int i = 0; i < sz_new_elems; i++) {
        new_list.push_back(new_elems_to_insert[i]);
    }

    cout << "new_list --> " << endl;
    new_list.print_list();
    new_list.alternating_split(out_list_a, out_list_b);
    cout << "after new_list.alternating_split(out_list_a, out_list_b) --> " << endl;
    cout << "out_list_a --> " << endl;
    out_list_a.print_list();
    cout << "out_list_b --> " << endl;
    out_list_b.print_list();
    cout << delim;
}

