#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    LinkedList<int> ll;
    string delim = string(20, '#') + '\n';
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;

    int i = 1;
    int n = 5;
    try {
        cout << "trying to insert elem " << n << " at index " << i << endl;
        ll.insert_nth(i, n);
    } catch (domain_error e) {
        cout << "caught exception --> " << e.what() << endl;
    }

    cout << delim;

    i = 0;
    cout << "trying to insert elem " << n << " at index " << i << endl;
    ll.insert_nth(i, n);
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;

    i = 0;
    n = 42;
    cout << "trying to insert elem " << n << " at index " << i << endl;
    ll.insert_nth(i, n);
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;

    i = 1;
    n = 56;
    cout << "trying to insert elem " << n << " at index " << i << endl;
    ll.insert_nth(i, n);
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;

    i = 3;
    n = 34;
    cout << "trying to insert elem " << n << " at index " << i << endl;
    ll.insert_nth(i, n);
    cout << "ll -> " << endl;
    ll.print_list();
    cout << delim;


}
