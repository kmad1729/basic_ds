#include "linked_list.h"
#include <string>
#include <iostream>

using namespace std;

int main()
{
    LinkedList<int> ll;
    string delim = string(20, '#') + '\n';
    ll.print_list();
    ll.push_back(1);
    ll.push_back(2);
    ll.push_back(3);
    ll.push_back(3);
    ll.push_back(3);
    ll.print_list();
    cout << "1 -> 2 -> 3 -> / << expected" << endl;

    cout << delim;
    int k = 2;
    cout << "count of " << k << " = " << ll.count(k) << endl;
    cout << "expected     1" << endl;

    k = 3;
    cout << "count of " << k << " = " << ll.count(k) << endl;
    cout << "expected     3" << endl;

    k = 5;
    cout << "count of " << k << " = " << ll.count(k) << endl;
    cout << "expected     0" << endl;

    ll.push_back(-1);
    ll.push_back(42);

    cout << delim;
    cout << "linked list --> " << endl;
    ll.print_list();

    int ind = 0;
    cout << "element at index [" << ind << "] =" << ll.get_nth(ind) << endl;
    cout << "expected             =1" << endl;

    ind = 3;
    cout << "element at index [" << ind << "] =" << ll.get_nth(ind) << endl;
    cout << "expected             =3" << endl;

    ind = 6;
    cout << "element at index [" << ind << "] =" << ll.get_nth(ind) << endl;
    cout << "expected             =42" << endl;

    ind = 5;
    cout << "element at index [" << ind << "] =" << ll.get_nth(ind) << endl;
    cout << "expected             =-1" << endl;

    try {
        cout << "trying to find elem at index 7" << endl;
        cout << "ll[7] = " << ll.get_nth(7) << endl;
    } catch(out_of_range e) {
        cout << "caught exception " << e.what() << endl;
    }
    cout << delim;

    LinkedList<string> ll2;
    ll2.push_back("batman");
    ll2.push_back("superman");
    cout << "ll2 --> " << endl;
    ll2.print_list();

    string s1 = ll2.pop();
    cout << "popped elem from ll2 -> (" << s1 << ")" << endl;
    cout << "expected             -> (batman)" << endl;

    s1 = ll2.pop();
    cout << "popped elem from ll2 -> (" << s1 << ")" << endl;
    cout << "expected             -> (superman)" << endl;

    cout << "ll2 --> " << endl;
    ll2.print_list();
    cout << " / <-- expected" << endl;

    try {
        cout << "trying to pop from empty list" << endl;
        cout << ll2.pop() << endl;
    } catch(domain_error e) {
        cout << "caught exception " << e.what() << endl;
    }

    cout << delim;


}
