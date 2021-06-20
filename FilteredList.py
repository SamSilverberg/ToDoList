class Linked_List:
    
    class __Node:
        
        def __init__(self, val):
            # Declare and initialize the public attributes for objects of the
            # Node class. TODO replace pass with your implementation
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self):
        # Declare and initialize the private attributes for objects of the
        # sentineled Linked_List class TODO replace pass with your
        # implementation
        self.__header = Linked_List.__Node(None)
        self.__trailer = Linked_List.__Node(None)
        self.__header.next = self.__trailer
        self.__trailer.prev = self.__header
        self.__size = 0

    def __len__(self):
        # Return the number of value-containing nodes in this list. TODO replace
        # pass with your implementation
        return self.__size

    def append_element(self, val):
        # Increase the size of the list by one, and add a node containing val at
        # the new tail position. this is the only way to add items at the tail
        # position. TODO replace pass with your implementation
        newest = Linked_List.__Node(val)
        newest.prev = self.__trailer.prev
        self.__trailer.prev.next = newest
        newest.next = self.__trailer
        self.__trailer.prev = newest
        self.__size = self.__size + 1

    def __walk(self, index):
        # a function used in index-based functions to walk from either side of the list
        k = 0
        if index == k:
            return self.__header  
        if index <= (self.__size/2): #first half 
            before_index = self.__header.next
            while k+1 != index: 
                before_index = before_index.next
                k = k+1
            return before_index
        else: #second half
            before_index = self.__trailer.prev
            k = self.__size-1
            while k != index-1:
                before_index = before_index.prev
                k = k-1
            return before_index

    def insert_element_at(self, val, index):
        # Assuming the head position (not the header node) is indexed 0, add a
        # node containing val at the specified index. If the index is not a
        # valid position within the list, raise an IndexError exception. This
        # method cannot be used to add an item at the tail position. TODO
        # replace pass with your implementation
        if index >= self.__size or index < 0: #can't append or out of bounds. Also takes care of size = 0
            raise IndexError
        newest = Linked_List.__Node(val)
        counter = self.__walk(index)
        newest.prev = counter
        newest.next = counter.next
        counter.next = newest
        newest.next.prev = newest
        self.__size = self.__size + 1

    def remove_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, remove
        # and return the value stored in the node at the specified index. If the
        # index is invalid, raise an IndexError exception. TODO replace pass
        # with your implementation
        if index >= self.__size or index < 0: 
            raise IndexError
        counter = self.__walk(index)
        to_return = counter.next.val
        counter.next.next.prev = counter
        counter.next = counter.next.next
        self.__size = self.__size - 1
        return to_return

    def get_element_at(self, index):
        # Assuming the head position (not the header node) is indexed 0, return
        # the value stored in the node at the specified index, but do not unlink
        # it from the list. If the specified index is invalid, raise an
        # IndexError exception. TODO replace pass with your implementation
        if index >= self.__size or index < 0: 
            raise IndexError
        count = self.__walk(index)
        return count.next.val

    def rotate_left(self):
        # Rotate the list left one position. Conceptual indices should all
        # decrease by one, except for the head, which should become the tail.
        # For example, if the list is [ 5, 7, 9, -4 ], this method should alter
        # it to [ 7, 9, -4, 5 ]. This method should modify the list in place and
        # must not return a value. TODO replace pass with your implementation.
       self.append_element(self.__header.next.val)
       self.remove_element_at(0)
        
    def __str__(self):
        # Return a string representation of the list's contents. An empty list
        # should appear as [ ]. A list with one element should appear as [ 5 ].
        # A list with two elements should appear as [ 5, 7 ]. You may assume
        # that the values stored inside of the node objects implement the
        # __str__() method, so you call str(val_object) on them to get their
        # string representations. TODO replace pass with your implementation
        if self.__size == 0:
            return('[ ]')
        new = [None]*self.__size 
        k = 0
        cur = self.__header.next
        while cur is not self.__trailer: 
            new[k] = str(cur.val)
            k += 1
            cur = cur.next
        num = ', '.join(new) 
        return f'[ {num} ]'

    def __iter__(self):
        # Initialize a new attribute for walking through your list TODO insert
        # your initialization code before the return statement. Do not modify
        # the return statement.
        self.__iter_start = self.__header.next
        return self

    def __next__(self):
        # Using the attribute that you initialized in __iter__(), fetch the next
        # value and return it. If there are no more values to fetch, raise a
        # StopIteration exception. TODO replace pass with your implementation
        if self.__iter_start is self.__trailer:
            raise StopIteration
        control_var = self.__iter_start.val
        self.__iter_start = self.__iter_start.next
        return control_var

    def __reversed__(self):
        # Construct and return a new Linked_List object whose nodes alias the
        # same objects as the nodes in this list, but in reverse order. For a
        # Linked_List object ll, Python will automatically call this function
        # when it encounters a call to reversed(ll) in an application. If
        # print(ll) displays [ 1, 2, 3, 4, 5 ], then print(reversed(ll)) should
        # display [ 5, 4, 3, 2, 1 ]. This method does not change the state of
        # the object on which it is called. Calling print(ll) again will still
        # display [ 1, 2, 3, 4, 5 ], even after calling reversed(ll). This
        # method must operate in linear time.
        rev = Linked_List()
        count = self.__trailer
        while count.prev is not self.__header:
            count = count.prev
            rev.append_element(count.val)
        return rev

if __name__ == '__main__':
    # Your test code should go here. Be sure to look at cases when the list is
    # empty, when it has one element, and when it has several elements. Do the
    # indexed methods raise exceptions when given invalid indices? Do they
    # position items correctly when given valid indices? Does the string
    # representation of your list conform to the specified format? Does removing
    # an element function correctly regardless of that element's location? Does
    # a for loop iterate through your list from head to tail? Does a for loop
    # iterate through your reversed list from tail to head? Your writeup should
    # explain why you chose the test cases. Leave all test cases in your code
    # when submitting. TODO replace pass with your tests
    test = Linked_List()
    
    assert str(test) == '[ ]' #test empty list formatting
    assert len(test) == 0 #test size

    try: #get value in empty list should raise an error
        test.get_element_at(0)
        test.get_element_at(-1)
        test.get_element_at(1)
    except IndexError:
        assert True

    test.append_element(10)
    assert str(test) == '[ 10 ]' #test 1 value list formatting
    assert len(test) == 1 #test size
    assert test.get_element_at(0) == 10 #check get_element works

    test.insert_element_at(8, 0)
    assert str(test) == '[ 8, 10 ]' #test 2+ value list formatting
    assert len(test) == 2 #test size
    assert test.get_element_at(0) == 8 #check get_element works

    test.insert_element_at(9, 1)
    assert str(test) == '[ 8, 9, 10 ]' #test 2+ value list formatting
    assert len(test) == 3 #test size
    assert test.get_element_at(2) == 10 #check get_element works

    test.append_element(11)
    assert str(test) == '[ 8, 9, 10, 11 ]' #test appending only works at the tail
    assert len(test) == 4 #test size

    try: #remove at an invalid index should raise an error
        test.remove_element_at(4)
        test.remove_element_at(-1)
    except IndexError:
        assert True
        assert str(test) == '[ 8, 9, 10, 11 ]' #should stay unchanged when error is raised
    
    try: #insert val 0 at invalid index shoudl raise error
        test.insert_element_at(0, -1) 
        test.insert_element_at(0, 4)
    except IndexError:
        assert True
        assert str(test) == '[ 8, 9, 10, 11 ]' #should stay unchanged when error is raised

    try: #get element at invalid index should raise error
        test.get_element_at(-1)
        test.get_element_at(5)
    except IndexError:
        assert True

    assert str(reversed(test)) == '[ 11, 10, 9, 8 ]' #check reversed
    assert str(test) == '[ 8, 9, 10, 11 ]' #check original is unchanged
    
    k = 0
    for i in test: #test that for loop returns correct values
        assert i == test.get_element_at(k)
        k += 1

    k = 0
    for i in reversed(test): #test that for loop returns correct values on reversed list
        assert i == reversed(test).get_element_at(k)
        k += 1

    test.rotate_left() #check rotation 1) rotates and 2) modifies original list
    assert str(test) == '[ 9, 10, 11, 8 ]'
    test.rotate_left() #rotate again
    assert str(test) == '[ 10, 11, 8, 9 ]'
    assert len(test) == 4

    test.remove_element_at(0)
    test.remove_element_at(2)
    test.remove_element_at(1)
    test.remove_element_at(0) #empty list now
    assert len(test) == 0 #check empty
    test.rotate_left() #check that it doesn't fail on an empty list
    assert str(test) == '[ ]'


