class Linked_List:
   
   class __Node:
      
      def __init__(self, val):
         self.val = val
         self.next = None
         self.prev = None
       # declare and initialize the public attributes
       # for objects of the Node class.
       # TODO replace pass with your implementation

   def __init__(self):
      self.__size = 0
      self.__header = Linked_List.__Node(None)
      self.__trailer = Linked_List.__Node(None)
      self.__header.next = self.__trailer
      self.__trailer.prev = self.__header
     # declare and initialize the private attributes
     # for objects of the sentineled Linked_List class
     # TODO replace pass with your implementation
     

   def __len__(self):
      return self.__size
     # return the number of value-containing nodes in 
     # this list.
     # TODO replace pass with your implementation

   def append_element(self, val):
      append = Linked_List.__Node(val)
      append.next = self.__trailer 
      append.prev = self.__trailer.prev
      self.__trailer.prev.next = append
      self.__trailer.prev = append
      self.__size += 1
      # increase the size of the list by one, and add a
      # node containing val at the new tail position. this 
      # is the only way to add items at the tail position.
      # TODO replace pass with your implementation

   def insert_element_at(self, val, index):
      insert = Linked_List.__Node(val)
      if index >= self.__size or index < 0:
         raise IndexError 
                              
      if index <= self.__size // 2: #first half of list
         cur = self.__header
         for i in range(index):
            cur = cur.next
      else: #second half of list
         cur = self.__trailer.prev
         for i in range(self.__size - index):
            cur = cur.prev
      insert.next = cur.next
      insert.prev = cur
      cur.next.prev = insert
      cur.next = insert
      self.__size += 1 
      # assuming the head position (not the header node)
      # is indexed 0, add a node containing val at the 
      # specified index. If the index is not a valid 
      # position within the list, raise an IndexError 
      # exception. This method cannot be used to add an 
      # item at the tail position.
      # TODO replace pass with your implementation
     
   def remove_element_at(self, index):
      if index >= len(self) or index < 0:
         raise IndexError
         
      if index >= self.__size // 2: #second half of list
         cur = self.__trailer
         for i in range(self.__size - (index + 1)):
            cur = cur.prev
         val = cur.prev.val
         cur.prev.next = None
         cur.prev.prev.next = cur
         cur.prev = cur.prev.prev
         self.__size -= 1
         return val
      else: #first half of list
         cur = self.__header
         for i in range(index):
            cur = cur.next
         val = cur.next.val
         cur.next.prev = None
         cur.next.next.prev = cur
         cur.next = cur.next.next
         self.__size -= 1
         return val
      # assuming the head position (not the header node)
      # is indexed 0, remove and return the value stored 
      # in the node at the specified index. If the index 
      # is invalid, raise an IndexError exception.
      # TODO replace pass with your implementation

   def get_element_at(self, index):
      if index >= len(self) or index < 0:
         raise IndexError
         
      if index >= self.__size // 2: #second half of list
         cur = self.__trailer
         for i in range(self.__size - index):
            cur = cur.prev
      else: #first half of list
         cur = self.__header.next
         for i in range(index):
            cur = cur.next
      return cur.val
      # assuming the head position (not the header node)
      # is indexed 0, return the value stored in the node 
      # at the specified index, but do not unlink it from 
      # the list. If the specified index is invalid, raise 
      # an IndexError exception.
      # TODO replace pass with your implementation

   def rotate_left(self):
      if self.__size <= 1:
         return
      cur = self.__header.next
      self.__header.next.next.prev = self.__header
      self.__header.next = cur.next
      cur.next = self.__trailer
      cur.prev = self.__trailer.prev
      self.__trailer.prev.next = cur
      self.__trailer.prev = cur
      # rotate the list left one position. Conceptual indices
      # should all decrease by one, except for the head, which
      # should become the tail. For example, if the list is
      # [ 5, 7, 9, -4 ], this method should alter it to
      # [ 7, 9, -4, 5 ]. This method should modify the list in
      # place and must not return a value.
      # TODO replace pass with your implementation.
     
   def __str__(self):
      if self.__size == 0:
         return '[ ]'
      list = '[ '
      cur = self.__header
      for i in range(len(self)):
         if i == len(self) - 1:
            list = list + str(cur.next.val) + ' ]'
            break
         list = list + str(cur.next.val) + ', '
         cur = cur.next
      return list
      # return a string representation of the list's
      # contents. An empty list should appear as [ ].
      # A list with one element should appear as [ 5 ].
      # A list with two elements should appear as [ 5, 7 ].
      # You may assume that the values stored inside of the
      # node objects implement the __str__() method, so you
      # call str(val_object) on them to get their string
      # representations.
      # TODO replace pass with your implementation

   def __iter__(self):
      self.__cur = self.__header.next
      # initialize a new attribute for walking through your list
      # TODO insert your initialization code before the return
      # statement. do not modify the return statement.
      return self

   def __next__(self):
      if self.__cur is self.__trailer:
         raise StopIteration
      val = self.__cur.val
      self.__cur = self.__cur.next
      return val
      # using the attribute that you initialized in __iter__(),
      # fetch the next value and return it. If there are no more 
      # values to fetch, raise a StopIteration exception.
      # TODO replace pass with your implementation        

if __name__ == '__main__':


   print('------append_element testcases------')
   #testcases check if size is updated correctly and if values get appended properly
   append_list = Linked_List()
   append_list.append_element(1)
   print('Append 1 into list:')
   print(append_list)
   print('list has ' + str(len(append_list)) + ' element')
   print()
   
   print('Append 2 into list:')
   append_list.append_element(2)
   print(append_list)
   print('list has ' + str(len(append_list)) + ' elements')
   print()
   
   print('Append 3 into list:')
   append_list.append_element(3)
   print(append_list)
   print('list has ' + str(len(append_list)) + ' elements')
   print()
   print()
   
   
   print('------insert_element_at testcases------')
   #testcases check if size is updated correctly, if values are inserted at proper indexes, and if index error check works properly
   insert_list = Linked_List()
   try:
      print('INSERT 0 AT INDEX 0:')
      insert_list.insert_element_at(0, 0)
   except IndexError:
      print('Error: index 0 out of bounds')
      print(insert_list)
      print('list has ' + str(len(insert_list)) + ' elements')
   print()
   
   print('STARTING LIST:')
   insert_list.append_element(3)
   print(insert_list)
   print('list has ' + str(len(insert_list)) + ' element')
   print()
   
   insert_list.insert_element_at(1, 0)
   print('INSERT 1 AT INDEX 0:')
   print(insert_list)
   print('list has ' + str(len(insert_list)) + ' elements')
   print()
   
   insert_list.insert_element_at(2, 1)
   print('INSERT 2 AT INDEX 1:')
   print(insert_list)
   print('list has ' + str(len(insert_list)) + ' elements')
   print()
   
   try:
      print('INSERT 4 AT INDEX 4:')
      insert_list.insert_element_at(4, 4)
   except IndexError:
      print('Error: index 5 out of bounds')
      print(insert_list)
      print('list has ' + str(len(insert_list)) + ' elements')
   print()
   
   try:
      print('INSERT -1 AT INDEX -1:')
      insert_list.insert_element_at(-1, -1)
   except IndexError:
      print('Error: index -1 out of bounds')
      print(insert_list)
      print('list has ' + str(len(insert_list)) + ' elements')
   print()
   print()
   
   
   print('------remove_element_at testcases------')
   #testcases to check if values are removed from list correctly, if sizes are updates correctly, and if index error checks work properly 
   remove_list = Linked_List()
   try:
      print('REMOVE VALUE AT INDEX 0:')
      remove_list.remove_element_at(0)
   except IndexError:
      print('Error: index 0 out of bounds')
      print(remove_list)
      print('list has ' + str(len(remove_list)) + ' elements')
      print()
      
   print('STARTING LIST:')
   remove_list.append_element(0)
   remove_list.append_element(1)
   remove_list.append_element(2)
   remove_list.append_element(3)
   print(remove_list)
   print('list has ' + str(len(remove_list)) + ' elements')
   print()
   
   print('REMOVE VALUE AT INDEX 0:')
   print(str(remove_list.remove_element_at(0)) + ' REMOVED FROM LIST')
   print(remove_list)
   print('list has ' + str(len(remove_list)) + ' elements')
   print()
   
   print('REMOVE VALUE AT INDEX 2:')
   print(str(remove_list.remove_element_at(2)) + ' REMOVED FROM LIST')
   print(remove_list)
   print('list has ' + str(len(remove_list)) + ' elements')
   print()
   
   try:
      print('REMOVE VALUE AT INDEX 3:')
      remove_list.remove_element_at(3)
   except IndexError:
      print('Error: index 3 out of bounds')
      print(remove_list)
      print('list has ' + str(len(remove_list)) + ' elements')
      print()
      
   try:
      print('REMOVE VALUE AT INDEX -1:')
      remove_list.remove_element_at(-1)
   except IndexError:
      print('Error: index -1 out of bounds')
      print(remove_list)
      print('list has ' + str(len(remove_list)) + ' elements')
      print()
   
   print('REMOVE VALUE AT INDEX 1:')
   print(str(remove_list.remove_element_at(1)) + ' REMOVED FROM LIST')
   print(remove_list)
   print('list has ' + str(len(remove_list)) + ' element')
   print()
   
   print('REMOVE VALUE AT INDEX 0:')
   print(str(remove_list.remove_element_at(0)) + ' REMOVED FROM LIST')
   print(remove_list)
   print('list has ' + str(len(remove_list)) + ' elements') 
   print()
   print()
   
   
   print('------iter & next textcases------')
   #testcase to check if traversing the linked list works properly
   list = Linked_List()
   print('EMPTY LIST:')
   print(list)
   print('Traversing list to print out each value in the list:')
   for val in list:
      print(val)
   print()
   
   print('LIST OF SIZE 1:')
   list.append_element(1)
   print(list)
   print('Traversing list to print out each value in the list:')
   for val in list:
      print(val)
   print()
   
   print('LIST OF MANY ELEMENTS:')
   list.append_element(2)
   list.append_element(3)
   list.append_element(4)
   list.append_element(5)
   print(list)
   print()
   print('Traversing list to print out each value in the list:')
   for val in list:
      print(val)
   print()
   print()
   
   print('------get_element_at testcases------')
   #testcases to check if method gets value at correct index and if index error check works properly
   get_list = Linked_List()
   try:
      print('GET THE VALUE AT INDEX 0:')
      get_list.get_element_at(0)
   except IndexError:
      print('Error: index 0 out of bounds')
      print(get_list)
      print()
   
   get_list.append_element(1)
   get_list.append_element(2)
   get_list.append_element(3)
   print('STARTING LIST:')
   print(get_list)
   print('list has ' + str(len(get_list)) + ' elements')
   print()
   print('GET VALUE AT INDEX 0:')
   print('value of ' + str(get_list.get_element_at(0)) + ' at index 0')
   print()
   print('GET VALUE AT INDEX 1:')
   print('value of ' + str(get_list.get_element_at(1)) + ' at index 1')
   print()
   print('GET VALUE AT INDEX 2:')
   print('value of ' + str(get_list.get_element_at(2)) + ' at index 2')
   print()
   try:
      print('GET THE VALUE INDEX 5:')
      get_list.get_element_at(5)
   except IndexError:
      print('Error: index 5 out of bounds')
      print(get_list)
      print()
      
   try:
      print('GET VALUE AT INDEX -1:')
      list.get_element_at(-1)
   except IndexError:
      print('Error: index -1 out of bounds')
      print(get_list)
   print()
   print()
   
   print('------rotate_left testcases------')
   #testcases to check if list is rotated left properly
   left_list = Linked_List()
   
   print('EMPTY LIST:')
   print(left_list)
   print()
   print('ROTATE LEFT:')
   left_list.rotate_left()
   print(left_list)
   print() 
   
   print('LIST OF SIZE 1:')
   left_list.append_element(1)
   print(left_list)
   print() 
   print('ROTATE LEFT:')
   left_list.rotate_left()
   print(left_list)
   print() 
   
   left_list.append_element(2)
   left_list.append_element(3)
   left_list.append_element(4)
   left_list.append_element(5)
   print('LIST OF MANY ELEMENTS:')
   print(left_list)
   print()
   
   print('ROTATE LEFT:')
   left_list.rotate_left()
   print(left_list)
   print()
   
   print('ROTATE LEFT:')
   left_list.rotate_left()
   print(left_list)
   print()
   
   
   # Your test code should go here. Be sure to look at cases
   # when the list is empty, when it has one element, and when 
   # it has several elements. Do the indexed methods raise exceptions
   # when given invalid indices? Do they position items
   # correctly when given valid indices? Does the string
   # representation of your list conform to the specified format?
   # Does removing an element function correctly regardless of that
   # element's location? Does a for loop iterate through your list
   # from head to tail? Your writeup should explain why you chose the
   # test cases. Leave all test cases in your code when submitting.
   # TODO replace pass with your tests