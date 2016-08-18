CC=g++
CC_Flags= -Wall -g

_ALL = test_max_heapify test_make_heap test_heap_sort

all: $(_ALL)

test_max_heapify: test_max_heapify.cc
	$(CC) $(CC_Flags) -o $@ $^

test_make_heap: test_make_heap.cc
	$(CC) $(CC_Flags) -o $@ $^

test_heap_sort: test_heap_sort.cc
	$(CC) $(CC_Flags) -o $@ $^

clean:
	rm -rf $(_ALL)
