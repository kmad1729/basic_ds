#pragma once
#include <iostream>
#include <stdexcept>

template <class T>
struct ListNode {
    T data;
    ListNode<T>* next;
    ListNode(const T& d) {
        data = T(d);
        next = NULL;
    }
};

template <class T>
class LinkedList {
    private:
        ListNode<T>* head;
        ListNode<T>* tail;

        void util_sorted_insert(ListNode<T>*& beg, ListNode<T>* n) {
            ListNode<T>* c_n;
            ListNode<T>* prev = NULL;
            for(c_n = beg; c_n != NULL; c_n = (c_n -> next)) {
                if((n -> data) <= (c_n -> data))
                    break;
                prev = c_n;
            }
            if(prev == NULL) {
                if(beg == NULL) {
                    beg = n;
                    tail = n;
                } else {
                    (n -> next) = beg;
                    beg = n;
                }
            } else {
                if(c_n == NULL) {
                    (prev -> next) = n;
                    tail = n;
                } else {
                    (n -> next) = c_n;
                    (prev -> next) = n;
                }
            }
        }

    public:
        LinkedList() {
            head = NULL;
            tail = NULL;
        }

        ~LinkedList() {
            while(head != NULL) {
                ListNode<T>* tmp = head;
                head = (head -> next);
                delete tmp;
            }
            tail = NULL;
        }

        void push_back(const T& d) {
            if(tail == NULL) {
                tail = new ListNode<T>(d);
                head = tail;
            } else {
                (tail -> next) = new ListNode<T>(d);
                tail = (tail -> next);
            }
        }

        void print_list() {
            if(head == NULL)
                std::cout << "empty list! " << std::endl;
            else {
                for(ListNode<T>* c_n = head; c_n != NULL; 
                        c_n = (c_n -> next))
                    std::cout << (c_n -> data) << " -> ";
                std::cout << "/" << std::endl;
            }
        }

        int count(const T& count_for) {
            int result = 0;
            for(ListNode<T>* ll_node = head; ll_node != NULL;
                    ll_node = (ll_node -> next))
                    if((ll_node -> data) == count_for)
                        result++;
            return result;
        }

        T& get_nth(int ind) {
            ListNode<T>* c_n = head;
            for(int i = 0; i < ind; i++) {
                if(c_n == NULL)
                    throw std::out_of_range("not enough elements!");
                c_n = (c_n -> next);
            }
            if(c_n == NULL)
                throw std::out_of_range("not enough elements!");
            return (c_n -> data);
        }

        T pop() {
            if(head == NULL)
                throw std::domain_error("cannot pop empty list!");
            ListNode<T>* ret_node = head;
            head = (head -> next);
            if(head == NULL) {
                tail = NULL;
            }
            T ret_val = (ret_node -> data);
            delete ret_node;
            return ret_val;
        }

        void insert_nth(int n, int data) {
            ListNode<T>* c_n = head;
            ListNode<T>* prev = NULL;
            for(int i = 0; i < n; i++) {
                if(c_n == NULL)
                    throw std::domain_error("cannot insert one past last elem");
                prev = c_n;
                c_n = (c_n -> next);
            }

            ListNode<T>* new_node = new ListNode<T>(data);
            if(c_n == NULL) {
                //empty list or last node
                if(head == NULL) {
                    head = new_node;
                    tail = new_node;
                } else {
                    (tail -> next) = new_node;
                    tail = new_node;
                }
            } else {
                //start of the list or somewhere in the middle
                if(prev == NULL) {
                    (new_node -> next) = head;
                    head = new_node;
                } else {
                    (new_node -> next) = c_n;
                    (prev -> next) = new_node;
                }
            }
        }

        void sorted_insert(int data) {
            ListNode<T>* n = new ListNode<T>(data);
            util_sorted_insert(head, n);
        }

        void insert_sort() {
            ListNode<T>* new_head = NULL;
            ListNode<T>* c_n;
            while(head != NULL) {
                c_n = head;
                head = (head -> next);
                (c_n -> next) = NULL;
                util_sorted_insert(new_head, c_n);
            }
            head = new_head;
        }

        void append(LinkedList<T>& other) {
            if(head == NULL) {
                head = other.head;
                tail = other.tail;
            } else {
                (tail -> next) = other.head;
                tail = other.tail;
            }
            other.head = NULL;
            other.tail = NULL;
        }

        /*
         * Split the nodes of a given list into front and back halves
         * and return the two lists using the reference params
         * If length is odd, extra node should go in the front list
         */
        void front_back_split(LinkedList<T>& front, LinkedList<T>& back) {
            ListNode<T>* slow_ptr = head;
            ListNode<T>* fast_ptr = head;
            if(slow_ptr == NULL)
                return;
            fast_ptr = (fast_ptr -> next);
            if(fast_ptr == NULL) {
                front.push_back((slow_ptr -> data));
                return;
            }

            slow_ptr = (slow_ptr -> next);
            fast_ptr = (fast_ptr -> next);
            while(fast_ptr != NULL) {
                slow_ptr = (slow_ptr -> next);
                fast_ptr = (fast_ptr -> next);
                if(fast_ptr == NULL)
                    break;
                fast_ptr = (fast_ptr -> next);
            }

            ListNode<T>* curr_ptr = head;
            while(curr_ptr != slow_ptr) {
                front.push_back((curr_ptr -> data));
                curr_ptr = (curr_ptr -> next);
            }

            while(curr_ptr != NULL) {
                back.push_back((curr_ptr -> data));
                curr_ptr = (curr_ptr -> next);
            }
        }

        /*
         * remove duplicates from a sorted list
         */
        void remove_duplicates() {
            if(head == NULL)
                return;
            ListNode<T>* curr = head;
            ListNode<T>* nxt = (curr -> next);
            ListNode<T>* tmp = NULL;
            while(nxt != NULL) {
                if((curr -> data) == (nxt -> data)) {
                    tmp = nxt;
                    nxt = (nxt -> next);
                    (curr -> next) = nxt;
                    delete tmp;
                } else {
                    curr = nxt;
                    nxt = (nxt -> next);
                }
            }
            tail = curr;

        }

        /*
         * Take the node from the front of other, and move it to
         * front of current list.
         * It is an error to call this with the source list empty
         */
        void move_node(LinkedList<T>& other) {
            if(other.head == NULL) {
                throw std::domain_error("other list is empty!");
            }
            ListNode<T>* tmp = other.head;
            (other.head) = ((other.head) -> next);
            (tmp -> next) = head;
            if(head == NULL)
                tail = tmp;
            head = tmp;
        }

        /*
         * shuffle_merge:
         *  merge nodes of the two lists int oa single list taking a node alternately
         *  from each list, and return the new list
         */
        void shuffle_merge(const LinkedList<T>& a, const LinkedList<T>& b) {
            int counter = 0;
            ListNode<T>* a_ptr = a.head;
            ListNode<T>* b_ptr = b.head;
            while(a_ptr != NULL && b_ptr != NULL) {
                if(counter % 2 == 0) {
                    push_back(a_ptr -> data);
                    a_ptr = (a_ptr -> next);
                } else {
                    push_back(b_ptr -> data);
                    b_ptr = (b_ptr -> next);
                }
                counter++;
            }

            ListNode<T>* rem_ptr = NULL;
            if(a_ptr == NULL)
                rem_ptr = b_ptr;
            else
                rem_ptr = a_ptr;
            while(rem_ptr != NULL) {
                push_back(rem_ptr -> data);
                rem_ptr = (rem_ptr -> next);
            }
        }

        /*
         * alternating_split:
         *  Given the source list, split its nodes into 2 shorter lists.
         */
        void alternating_split(LinkedList<T>& aRef, LinkedList<T>& bRef) {
            int counter = 0;
            for(ListNode<T>* curr = head; curr != NULL; curr = (curr -> next)) {
                if(counter % 2 == 0)
                    aRef.push_back(curr -> data);
                else
                    bRef.push_back(curr -> data);
                counter++;
            }
        }

        /*
         * sorted_merge:
         *  Takes 2 lists in increasing order and 
         *  splices their nodes together to make one big sorted list
         */
        void sorted_merge(const LinkedList<T>& a, const LinkedList<T>& b) {
            ListNode<T>* a_ptr = a.head;
            ListNode<T>* b_ptr = b.head;
            while(a_ptr != NULL && b_ptr != NULL) {
                if((a_ptr -> data) < (b_ptr -> data)) {
                    push_back(a_ptr -> data);
                    a_ptr = (a_ptr -> next);
                } else {
                    push_back(b_ptr -> data);
                    b_ptr = (b_ptr -> next);
                }
            }

            ListNode<T>* rem_ptr = NULL;
            if(a_ptr == NULL)
                rem_ptr = b_ptr;
            else
                rem_ptr = a_ptr;

            while(rem_ptr != NULL) {
                push_back(rem_ptr -> data);
                rem_ptr = (rem_ptr -> next);
            }
        }

        /*
         * merge_sort:
         *  write the classic recursive merge_sort
         */
        void merge_sort() {
            if(head != NULL && (head -> next) != NULL) {
                LinkedList<T> left;
                LinkedList<T> right;
                front_back_split(left, right);

                ListNode<T>* c_n = head;
                ListNode<T>* tmp = NULL;
                while(c_n != NULL) {
                    tmp = c_n;
                    c_n = (c_n -> next);
                    delete tmp;
                }
                head = tail = NULL;

                left.merge_sort();
                right.merge_sort();
                sorted_merge(left, right);
            }
        }

        /*
         * sorted_intersect:
         *  given 2 sorted lists. Create and represent a new list representing the 
         *  intersection of the two lists
         */
        void sorted_intersect(const LinkedList<T>& a, const LinkedList<T>& b) {
            ListNode<T>* a_ptr = a.head;
            ListNode<T>* b_ptr = b.head;
            while(a_ptr != NULL && b_ptr != NULL) {
                if((a_ptr -> data) < (b_ptr -> data))
                    a_ptr = (a_ptr -> next);
                else if((a_ptr -> data) > (b_ptr -> data))
                    b_ptr = (b_ptr -> next);
                else {
                    push_back(a_ptr -> data);
                    a_ptr = (a_ptr -> next);
                    b_ptr = (b_ptr -> next);
                }
            }
        }

        /*
         * reverse:
         *  reverse function that reverses a list by iteratively
         *  rearranging all the next pointers
         */
        void reverse() {
            ListNode<T>* new_head = NULL;
            ListNode<T>* new_tail = NULL;
            ListNode<T>* tmp = NULL;
            while(head != NULL) {
                tmp = head;
                head = (head -> next);
                if(new_head == NULL) {
                    (tmp -> next) = NULL;
                    new_head = tmp;
                    new_tail = tmp;
                } else {
                    (tmp -> next) = new_head;
                    new_head = tmp;
                }
            }

            head = new_head;
            tail = new_tail;
        }

        /*
         * util_recursive_reverse:
         *  utility function to reverse a linked list recursively.
         *  Reterns the end of the list after reversal
         */
        ListNode<T>* util_recursive_reverse(ListNode<T>* n) {
            if(n == NULL)
                return n;
            if((n -> next) == NULL)
                return n;
            ListNode<T>* new_tail = util_recursive_reverse(n -> next);
            (new_tail -> next) = n;
            return n;
        }

        void recursive_reverse() {
            if(head == NULL)
                return;
            ListNode<T>* new_tail = util_recursive_reverse(head);
            (new_tail -> next) = NULL;
            head = tail;
            tail = new_tail;
        }

        /*
         * reverse_sub_list:
         *  for given start and finish reverse the sublist [start, finish)
         */
        void reverse_sub_list(int start, int finish) {
        }

};
