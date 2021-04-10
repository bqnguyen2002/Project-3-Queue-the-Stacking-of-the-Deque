from Deque import Deque

class Array_Deque(Deque):

   def __init__(self):
      # capacity starts at 1; we will grow on demand.
      self.__capacity = 1
      self.__contents = [None] * self.__capacity
      self.__front = None #index of the front of the array deque
      self.__back = None #index of the back of the array deque
      self.__size = 0
     # TODO replace pass with any additional initializations you need.
     
   def __str__(self):
      # TODO replace pass with an implementation that returns a string of
      # exactly the same format as the __str__ method in the Linked_List_Deque.
      if self.__size == 0:
         return ('[ ]')
      reordered_contents = '[ ' 
      index = self.__front
      for i in range(self.__size):
         if index == self.__capacity: #if the index of front reaches the end of the array deque, it wraps around to index 0 
            index = 0
         if i == self.__size - 1: #once the final item in self.__contents has been reached, no more commas are added and an end brace is added to the string
            reordered_contents = reordered_contents + str(self.__contents[index]) + ' ]'
            break
         reordered_contents = reordered_contents + str(self.__contents[index]) + ', ' #adds an item from self.__contents to reordered_contents
         index+=1
      return reordered_contents #reordered contents is the contents of array deque reordered in a string format from front to back
     
   def __len__(self):
      # TODO replace pass with an implementation that returns the number of
      # items in the deque. This method must run in constant time.
      return self.__size

   def __grow(self):
      # TODO replace pass with an implementation that doubles the capacity
      # and positions existing items in the deque starting in cell 0 (why is
      # necessary?)
      self.__capacity = self.__capacity * 2
      new_contents = [None] * self.__capacity
      index = 0
      for i in range(self.__front, self.__front + self.__size):
         new_contents[index] = self.__contents[i % self.__size] #repositions self.__contents to have the front value be at index 0 in the new contents and back value be at index self.__size - 1
         index+=1
      self.__contents = new_contents
      self.__front = 0
      self.__back = self.__size - 1
      return self.__contents
     
   def push_front(self, val):
      # TODO replace pass with your implementation, growing the array before
      # pushing if necessary.
      if self.__size == self.__capacity:
         self.__grow()    
      if self.__size == 0:
         self.__front = 0
         self.__back = 0
         self.__contents[self.__front] = val
         self.__size += 1   
      elif self.__front == 0:
         self.__front = self.__capacity - 1
         self.__contents[self.__front] = val
         self.__size += 1
      else:
         self.__front -= 1
         self.__contents[self.__front] = val
         self.__size += 1
         
   def pop_front(self):
      # TODO replace pass with your implementation. Do not reduce the capacity.
      if self.__size == 0:
         return None
      temp = self.__contents[self.__front]
      if self.__size == 1:
         self.__front = None
         self.__back = None
         self.__size = 0
         return temp  
      self.__front += 1
      self.__size -= 1
      if self.__front == self.__capacity:
         self.__front = 0
      return temp
           
   def peek_front(self):
      # TODO replace pass with your implementation.
      if self.__size == 0:
         return None
      return self.__contents[self.__front]
     
   def push_back(self, val):
      # TODO replace pass with your implementation, growing the array before
      # pushing if necessary.
      if self.__size == self.__capacity:
         self.__grow()   
      if self.__size == 0:
         self.__front = 0
         self.__back = 0
         self.__contents[self.__front] = val
         self.__size += 1   
      else:
         self.__back += 1
         self.__contents[self.__back] = val
         self.__size += 1
   
   def pop_back(self):
      # TODO replace pass with your implementation. Do not reduce the capacity.
      if self.__size == 0:
         return None
      temp = self.__contents[self.__back]
      if self.__size == 1: 
         self.__front = None
         self.__back = None
         self.__size = 0 
         return temp
      self.__back -= 1
      self.__size -= 1
      if self.__back < 0:
         self.__back = self.__capacity
      return temp

   def peek_back(self):
      # TODO replace pass with your implementation.
      if self.__size == 0:
         return None
      return self.__contents[self.__back]


# No main section is necessary. Unit tests take its place.
#if __name__ == '__main__':
#pass

   




   
    
