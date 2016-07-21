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
};
