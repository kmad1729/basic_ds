CC=g++
CC_Flags= -Wall -g

_ALL = test_heap

all: $(_ALL)

test_heap: test_heap.cc
	$(CC) $(CC_Flags) -o $@ $^

clean:
	rm -rf $(_ALL)
