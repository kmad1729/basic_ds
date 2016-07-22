CC=g++
CC_Flags = -g -Wall

_ALL = test1_linked_list test2_linked_list test3_linked_list \
	   test4_linked_list

all: $(_ALL)

test1_linked_list: test1_linked_list.cc
	$(CC) $(CC_Flags) -o $@ $^

test2_linked_list: test2_linked_list.cc
	$(CC) $(CC_Flags) -o $@ $^

test3_linked_list: test3_linked_list.cc
	$(CC) $(CC_Flags) -o $@ $^

test4_linked_list: test4_linked_list.cc
	$(CC) $(CC_Flags) -o $@ $^

clean:
	rm -rf $(_ALL)
