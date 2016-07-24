#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    LinkedList<int> ll1;
    LinkedList<int> front1;
    LinkedList<int> back1;
    string delim = string(20, '#') + '\n';

    ll1.front_back_split(front1, back1);
    cout << "front_back_split of empty list -->" << endl;
    cout << "ll1 -> " << endl;
    ll1.print_list();
    cout << "front1 -> " << endl;
    front1.print_list();
    cout << "back1 ->" << endl;
    back1.print_list();
    cout << delim;

    int elems_to_insert1[] = {7, 5, 42, 6};
    int sz_elems1 = sizeof(elems_to_insert1) / sizeof(elems_to_insert1[0]);
    int d;
    for(int i = 0; i < sz_elems1; i++) {
        d = elems_to_insert1[i];
        ll1.push_back(d);
    }

    ll1.front_back_split(front1, back1);
    cout << "front_back_split of even size list --" << endl;
    cout << "ll1 -> " << endl;
    ll1.print_list();
    cout << "front1 -> " << endl;
    front1.print_list();
    cout << "back1 ->" << endl;
    back1.print_list();
    cout << delim;

    LinkedList<int> ll2;
    LinkedList<int> front2;
    LinkedList<int> back2;

    int elems_to_insert2[] = {7};
    int sz_elems2 = sizeof(elems_to_insert2) / sizeof(elems_to_insert2[0]);
    for(int i = 0; i < sz_elems2; i++) {
        d = elems_to_insert2[i];
        ll2.push_back(d);
    }

    ll2.front_back_split(front2, back2);
    cout << "front_back_split of single elem list --" << endl;
    cout << "ll2 -> " << endl;
    ll2.print_list();
    cout << "front2 -> " << endl;
    front2.print_list();
    cout << "back2 ->" << endl;
    back2.print_list();
    cout << delim;

    LinkedList<int> ll3;
    LinkedList<int> front3;
    LinkedList<int> back3;

    int elems_to_insert3[] = {7, 42, 37, 22, 89};
    int sz_elems3 = sizeof(elems_to_insert3) / sizeof(elems_to_insert3[0]);
    for(int i = 0; i < sz_elems3; i++) {
        d = elems_to_insert3[i];
        ll3.push_back(d);
    }

    ll3.front_back_split(front3, back3);
    cout << "front_back_split of odd size list --" << endl;
    cout << "ll3 -> " << endl;
    ll3.print_list();
    cout << "front3 -> " << endl;
    front3.print_list();
    cout << "back3 ->" << endl;
    back3.print_list();
    cout << delim;
}
