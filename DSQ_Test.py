import unittest
from Deque_Generator import get_deque
from Stack import Stack
from Queue import Queue

class DSQTester(unittest.TestCase):
   
   def setUp(self):
      self.__deque = get_deque()
      self.__stack = Stack()
      self.__queue = Queue()
      
      
   #_________STACK TEST CASES_____________
   
   
   #_________EMPTY STACK TESTS_____________
   
   def test_empty_stack_len(self):
      self.assertEqual(0, len(self.__stack))
   
   #tests size of an empty stack
   
   def test_empty_stack_str(self):
      self.assertEqual('[ ]', str(self.__stack)) 
   
   #tests string representation of an empty stack
   
   def test_empty_stack_pop_len(self):
      self.__stack.pop()
      self.assertEqual(0, len(self.__stack))
      
   #tests size of an empty stack after trying to pop off a value
   
   def test_empty_stack_pop_str(self):
      self.__stack.pop()
      self.assertEqual('[ ]', str(self.__stack))
      
   #tests string representation of an empty stack after trying to pop off a value
    
   def test_empty_stack_pop_return(self):
      self.assertEqual(None, self.__stack.pop())
      
   #tests returned value after a pop method is called by an empty stack
   
   def test_empty_stack_peek_return(self):
      self.assertEqual(None, self.__stack.peek()) 
      
   #tests returned value after a peek function is called by an empty stack
   
   #_________________________________________________________________________________________
   
   
   
   #_________PUSH TESTS_____________(first value in the list = top of the stack | last value in the list = bottom of the stack)
   
   def test_push_stack_str(self):
      self.__stack.push(1)
      self.assertEqual('[ 1 ]', str(self.__stack))
      
   #tests if push adds a value into a stack
   
   def test_push3_stack_str(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))

   #tests if push adds values in the correct order
   
   def test_push_stack_len(self):
      self.__stack.push(1)
      self.assertEqual(1, len(self.__stack))
   
   #tests size of a stack after a value has been pushed into it
   
   def test_push3_stack_len(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.assertEqual(3, len(self.__stack))
   
   #tests size of a stack after many values have been pushed into it
   
   #_________________________________________________________________________________________
   
   
   #_________POP TESTS_____________
   
   def test_pop_push_stack_return(self):
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.pop())
      
   #tests if returned value after a pop method is the value from a stack with a value pushed into it
   
   def test_pop_push3_stack_return(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.pop())
      
   #tests if returned value after a pop method is the value from the top of a stack with many values pushed into it
   
   def test_pop3_push3_stack_return(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.pop()
      self.__stack.pop()
      self.assertEqual(3, self.__stack.pop())
      
   #tests if returned value after many pop methods is the value from the bottom of a stack with many values pushed into it
   
   def test_pop_push_stack_str(self):
      self.__stack.push(1)
      self.__stack.pop()
      self.assertEqual('[ ]', str(self.__stack))
      
   #tests if pop removes a value from a stack with a value pushed into it
   
   def test_pop_push3_stack_str(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.pop()
      self.assertEqual('[ 2, 3 ]', str(self.__stack))
   
   #tests if pop removes the value from the top of a stack with many values pushed into it
   
   def test_pop3_push3_stack_str(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.pop()
      self.__stack.pop()
      self.__stack.pop()
      self.assertEqual('[ ]', str(self.__stack))
   
   #tests if pop removes all the values from a stack with many values pushed into it
   
   def test_pop_push_stack_len(self):
      self.__stack.push(1)
      self.__stack.pop()
      self.assertEqual(0, len(self.__stack))
      
   #tests size of a stack after popping a value off a stack with a value pushed into it
   
   def test_pop_push3_stack_len(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.pop()
      self.assertEqual(2, len(self.__stack))
   
   #tests size of a stack after popping a value off a stack with many values pushed into it
   
   def test_pop3_push3_stack_len(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.pop()
      self.__stack.pop()
      self.__stack.pop()
      self.assertEqual(0, len(self.__stack))
   
   #tests size of a stack after popping many values off a stack with many values pushed into it
   #_________________________________________________________________________________________________________
   
  
    
   #_________PEEK TESTS_____________
      
   def test_peek_push_stack_return(self):
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.peek())
      
   #tests peek function of a stack after a value has been pushed into it
    
   def test_peek_push3_stack_return(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.assertEqual(1, self.__stack.peek())
      
   #tests if peek returns value from the top of a stack
   
   def test_peek_push_stack_str(self):
      self.__stack.push(1)
      self.__stack.peek()
      self.assertEqual('[ 1 ]', str(self.__stack))
      
   #tests that peek function does not change the contents of a stack with a value pushed into it
   
   def test_peek_push3_stack_str(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.peek()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__stack))
      
   #tests that peek function does not change the contents of a stack with many values pushed into it
   
   def test_peek_push_stack_len(self):
      self.__stack.push(1)
      self.__stack.peek()
      self.assertEqual(1, len(self.__stack))
      
   #tests that peek function does not change the length of a stack with a value pushed into it
   
   def test_peek_push3_stack_len(self):
      self.__stack.push(3)
      self.__stack.push(2)
      self.__stack.push(1)
      self.__stack.peek()
      self.assertEqual(3, len(self.__stack))
      
   #tests that peek function does not change the length of a stack with many values pushed into it 
   #________________________________________________________________________________________________
   
   
   
   
   
   
   #_________QUEUE TEST CASES_____________(first value in the list = front of the queue | last value in the list = back of the queue)
   
  
   #_________EMPTY QUEUE TESTS_____________
   
   def test_empty_queue_len(self):
      self.assertEqual(0, len(self.__queue))
   
   #tests size of an empty queue
   
   def test_empty_queue_str(self):
      self.assertEqual('[ ]', str(self.__queue)) 
   
   #tests string representation of an empty queue
   
   def test_empty_queue_dequeue_len(self):
      self.__queue.dequeue()
      self.assertEqual(0, len(self.__queue))
      
   #tests size of a queue after dequeuing a value from an empty queue
   
   def test_empty_queue_dequeue_str(self):
      self.__queue.dequeue()
      self.assertEqual('[ ]', str(self.__queue))
      
   #tests string representation of a queue after trying to dequeue a value in an empty queue
   
   def test_empty_queue_dequeue_return(self):
      self.assertEqual(None, self.__queue.dequeue())
      
   #tests returned value after a dequeue method is called by an empty queue
   
   def test_empty_queue_peek_return(self):
      self.assertEqual(None, self.__queue.peek()) 
      
   #tests peek function of an empty queue
   #____________________________________________________________
   
   
   
   #_________ENQUEUE TESTS_____________
   
   def test_enqueue_queue_str(self):
      self.__queue.enqueue(1)
      self.assertEqual('[ 1 ]', str(self.__queue))
      
   #tests if enqueue adds a value into a queue
   
   def test_enqueue3_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))

   #tests if enqueue adds values in the correct order
   
   def test_enqueue_queue_len(self):
      self.__queue.enqueue(1)
      self.assertEqual(1, len(self.__queue))
   
   #tests size of a queue after a value has been enqueued into it
   
   def test_enqueue3_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(1)
      self.__queue.enqueue(1)
      self.assertEqual(3, len(self.__queue))
   
   #tests size of a queue after many values have been enqueued into it
   
   #_________________________________________________________________________________________
   
   
   
   #_________DEQUEUE TESTS_____________
   
   def test_dequeue_enqueue_queue_return(self):
      self.__queue.enqueue(1)
      self.assertEqual(1, self.__queue.dequeue())
      
   #tests if returned value after a dequeue method is the value from a queue with a value enqueued into it
      
   def test_dequeue_enqueue3_queue_return(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.assertEqual(1, self.__queue.dequeue())
      
   #tests if returned value after a dequeue method is the value from the front of a queue with many values enqueued into it
   
   def test_dequeue3_enqueue3_queue_return(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.dequeue()
      self.__queue.dequeue()
      self.assertEqual(3, self.__queue.dequeue())
      
   #tests if returned value after many dequeue methods is the value from the back of a queue with many values enqueued into it
   
   def test_dequeue_enqueue_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.dequeue()
      self.assertEqual('[ ]', str(self.__queue))
      
   #tests if dequeue removes a value from a queue with a value enqueued into it
   
   def test_dequeue_enqueue3_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.dequeue()
      self.assertEqual('[ 2, 3 ]', str(self.__queue))
   
   #tests if dequeue removes the value from the front of a queue with many values enqueued into it
   
   def test_dequeue3_enqueue3_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.dequeue()
      self.__queue.dequeue()
      self.__queue.dequeue()
      self.assertEqual('[ ]', str(self.__queue))
   
   #tests if dequeue removes all the values from a queue with many values enqueued into it
         
   def test_dequeue_enqueue_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.dequeue()
      self.assertEqual(0, len(self.__queue))
      
   #tests size of a queue after dequeuing a value off a queue with a value enqueued into it
   
   def test_dequeue_enqueue3_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.dequeue()
      self.assertEqual(2, len(self.__queue))
   
   #tests size of a queue after dequeuing a value off a queue with many values enqueued into it
   
   def test_dequeue3_enqueue3_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.dequeue()
      self.__queue.dequeue()
      self.__queue.dequeue()
      self.assertEqual(0, len(self.__queue))
   
   #tests size of a queue after dequeuing all values off a queue with many values enqueued into it
   #_________________________________________________________________________________________________________
   
  
    
   #_________PEEK TESTS_____________
      
   def test_peek_enqueue_queue_return(self):
      self.__queue.enqueue(1)
      self.assertEqual(1, self.__queue.peek())
      
   #tests peek function of a queue after a value has been enqueued into a queue it
   
   def test_peek_enqueue3_queue_return(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.assertEqual(1, self.__queue.peek())
      
   #tests if peek returns value from the front of a queue
   
   def test_peek_enqueue_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.peek()
      self.assertEqual('[ 1 ]', str(self.__queue))
      
   #tests that peek function does not change the contents of a queue with a value enqueued into it
      
   def test_peek_enqueue3_queue_str(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.peek()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__queue))  
      
   #tests that peek function does not change the contents of a queue with many values enqueued into it
   
   def test_peek_enqueue_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.peek()
      self.assertEqual(1, len(self.__queue))
      
   #tests that peek function does not change the size of a queue with a value enqueued into it
   
   def test_peek_enqueue3_queue_len(self):
      self.__queue.enqueue(1)
      self.__queue.enqueue(2)
      self.__queue.enqueue(3)
      self.__queue.peek()
      self.assertEqual(3, len(self.__queue))
      
   #tests that peek function does not change the size of a queue with many values enqueued into it 
   #________________________________________________________________________________________________
   
   
   
   
   

   #_________DEQUE TEST CASES_____________(first value in the list = front of the deque | last value in the list = back of the deque) 
   
   
   #_________EMPTY DEQUE TESTS_____________
   
   def test_empty_deque_len(self):
      self.assertEqual(0, len(self.__deque))
   
   #tests size of an empty deque
   
   def test_empty_deque_str(self):
      self.assertEqual('[ ]', str(self.__deque)) 
   
   #tests string representation of an empty deque
   
   def test_empty_deque_popfront_len(self):
      self.__deque.pop_front()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of an empty deque after trying to pop off a value from the front
   
   def test_empty_deque_popback_len(self):
      self.__deque.pop_back()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of an empty deque after trying to pop off a value from the back
   
   def test_empty_deque_popfront_str(self):
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests string representation of an empty deque after trying to pop off a value from the front
   
   def test_empty_deque_popback_str(self):
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests string representation of an empty deque after trying to pop off a value from the back
    
   def test_empty_deque_popfront_return(self):
      self.assertEqual(None, self.__deque.pop_front())
      
   #tests returned value after a pop front method is called by an empty deque
   
   def test_empty_deque_popback_return(self):
      self.assertEqual(None, self.__deque.pop_back())
      
   #tests returned value after a pop back method is called by an empty deque
   
   def test_empty_deque_peekfront_return(self):
      self.assertEqual(None, self.__deque.peek_front()) 
      
   #tests returned value after a peek front function is called by an empty deque
   
   def test_empty_deque_peekback_return(self):
      self.assertEqual(None, self.__deque.peek_back()) 
      
   #tests returned value after a peek back function is called by an empty deque
   #____________________________________________________________
   
   #_________PUSH FRONT TESTS_____________
   
   def test_pushfront_deque_str(self):
      self.__deque.push_front(1)
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests if push front adds a value into a deque
   
   def test_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

   #tests if push front adds values in the correct order
   
   def test_pushfront_deque_len(self):
      self.__deque.push_front(1)
      self.assertEqual(1, len(self.__deque))
   
   #tests size of a deque after a value has been pushed to the front of it
   
   def test_pushfront3_deque_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual(3, len(self.__deque))
   
   #tests size of a deque after many value has been pushed to the front of it
   
   #_________________________________________________________________________________________
   
   #_________PUSH BACK TESTS_____________
   
   def test_pushback_deque_str(self):
      self.__deque.push_back(1)
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests if push back adds a value into a deque
   
   def test_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))

   #tests if push back adds values in the correct order
   
   def test_pushback_deque_len(self):
      self.__deque.push_back(1)
      self.assertEqual(1, len(self.__deque))
   
   #tests size of a deque after a value has been pushed to the back of it
   
   def test_pushback3_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual(3, len(self.__deque))
   
   #tests size of a deque after many value has been pushed to the back of it
   #_________________________________________________________________________________________
   
   #_________POP FRONT TESTS_____________
   
   def test_popfront_pushfront_deque_return(self):
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.pop_front())
      
   #tests if returned value after a pop front method is the value from a deque with a value pushed to the front of it
   
   def test_popfront_pushback_deque_return(self):
      self.__deque.push_back(1)
      self.assertEqual(1, self.__deque.pop_front())
      
   #tests if returned value after a pop front method is the value from a deque with a value pushed to the back of it
      
   def test_popfront_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.pop_front())
      
   #tests if returned value after a pop front method is the value from the front of a deque with many values pushed to the front of it
   
   def test_popfront3_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual(3, self.__deque.pop_front())
      
   #tests if returned value after many pop front methods is the value from the back of a deque with many values pushed to the front of it
   
   def test_popfront_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual(1, self.__deque.pop_front())
      
   #tests if returned value after a pop front method is the value from the front of a dqeue with many values pushed to the back of it
   
   def test_popfront3_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual(3, self.__deque.pop_front())
      
   #tests if returned value after many pop front methods is the value from the front of a deque with many values pushed to the front of it
   
   def test_popfront_pushfront_deque_str(self):
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests if pop front removes a value from a deque with a value pushed to the front of it
   
   def test_popfront_pushback_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests if pop front removes a value from a deque with a value pushed to the back of it
   
   def test_popfront_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual('[ 2, 3 ]', str(self.__deque))
   
   #tests if pop front removes the value from the front of a deque with many values pushed to the front of it
   
   def test_popfront3_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
   
   #tests if many pop front calls removes all the values from a deque with three values pushed to the front of a deque
   
   def test_popfront_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_front()
      self.assertEqual('[ 2, 3 ]', str(self.__deque))
   
   #tests if pop front removes the value from the front of a deque with many values pushed to the back of it
   
   def test_popfront3_pushfront3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual('[ ]', str(self.__deque))
   
   #tests if many pop front calls removes all the values from a deque with three values pushed to the back of a deque
         
   def test_popfront_pushfront_deque_len(self):
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of a deque after popping a value off of the front after a value has been pushed to the front
   
   def test_popfront_pushback_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.pop_front()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of a deque after popping a value off of the front after a value has been pushed to the back
   
   def test_popfront_pushfront3_queue_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.assertEqual(2, len(self.__deque))
   
   #tests size of a deque after popping a value off the front after many values have been pushed to the front
   
   def test_popfront3_pushfront3_queue_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual(0, len(self.__deque))
   
   #tests size of a deque after popping all the values off the front after many values have been pushed to the front
   
   def test_popfront_pushback3_queue_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_front()
      self.assertEqual(2, len(self.__deque))
   
   #tests size of a deque after popping a value off the front after many values have been pushed to the back
   
   def test_popfront3_pushback3_queue_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.__deque.pop_front()
      self.assertEqual(0, len(self.__deque))
   
   #tests size of a deque after popping all the values off the front after many values have been pushed to the back
   
   #_________________________________________________________________________________________________________
   
   #_________POP BACK TESTS_____________
   
   def test_popback_pushfront_deque_return(self):
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.pop_back())
      
   #tests if returned value after a pop back method is the value from a deque with a value pushed to the front of it
   
   def test_popback_pushback_deque_return(self):
      self.__deque.push_back(1)
      self.assertEqual(1, self.__deque.pop_back())
      
   #tests if returned value after a pop back method is the value from a deque with a value pushed to the back of it
      
   def test_popback_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual(3, self.__deque.pop_back())
      
   #tests if returned value after a pop back method is the value from the back of a deque with many values pushed to the front of it
   
   def test_popback3_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual(1, self.__deque.pop_back())
      
   #tests if returned value after many pop back methods is the value from the back of a deque with many values pushed to the front of it
   
   def test_popback_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual(3, self.__deque.pop_back())
      
   #tests if returned value after a pop back method is the value from the front of a deque with many values pushed to the back of it
   
   def test_popback3_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual(1, self.__deque.pop_back())
      
   #tests if returned value after many pop back method is the value from the front of a deque with many values pushed to the back of it
   
   def test_popback_pushfront_deque_str(self):
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests if pop back removes a value from a deque with a value pushed to the front of it
   
   def test_popback_pushback_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
      
   #tests if pop back removes a value from a deque with a value pushed to the back of it
   
   def test_popback_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual('[ 1, 2 ]', str(self.__deque))
   
   #tests if pop back removes the value from the back of a deque with many values pushed to the front of it
   
   def test_popback3_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
   
   #tests if many pop back calls removes all the values from a deque with many values pushed to the front of it
   
   def test_popback_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_back()
      self.assertEqual('[ 1, 2 ]', str(self.__deque))
   
   #tests if pop back removes the value from the back of a deque with many values pushed to the back of it
   
   def test_popback3_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual('[ ]', str(self.__deque))
   
   #tests if many pop back calls removes all the values from a deque with many values pushed to the back of it
         
   def test_popback_pushfront_deque_len(self):
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of a deque after popping a value off of the back after a value has been pushed to the front of it
   
   def test_popback_pushback_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.pop_back()
      self.assertEqual(0, len(self.__deque))
      
   #tests size of a deque after popping a value off of the back after a value has been pushed to the back of it
   
   def test_popback_pushfront3_queue_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.assertEqual(2, len(self.__deque))
   
   #tests size of a deque after popping a value off the back after many values have been pushed to the front of it
   
   def test_popback3_pushfront3_queue_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual(0, len(self.__deque))
   
   #tests size of a deque after popping all the values off the back after many values have been pushed to the front of it
   
   def test_popback_pushback3_queue_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_back()
      self.assertEqual(2, len(self.__deque))
   
   #tests size of a deque after popping a value off the back after many values have been pushed to the back of it
   
   def test_popback3_pushback3_queue_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.__deque.pop_back()
      self.assertEqual(0, len(self.__deque))
   
   #tests size of a deque after popping a value off the back after many values have been pushed to the back of it
   #_________________________________________________________________________________________________________
   
   #_________PEEK FRONT TESTS_____________
      
   def test_peekfront_pushfront_deque_return(self):
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.peek_front())
      
   #tests peek front function of a deque after a value has been pushed to the front of it
   
   def test_peekfront_pushback_deque_return(self):
      self.__deque.push_back(1)
      self.assertEqual(1, self.__deque.peek_front())
      
   #tests peek front function of a deque after a value has been pushed to the back of it 
   
   def test_peekfront_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.peek_front())
      
   #tests if peek front returns value from the front of a deque after many values have been pushed to the front of it
   
   def test_peekfront_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual(1, self.__deque.peek_front())
      
   #tests if peek front returns value from the front of a deque after many values have been pushed to the back of it 
   
   def test_peekfront_pushfront_deque_str(self):
      self.__deque.push_front(1)
      self.__deque.peek_front()
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests that the peek front function does not change the contents of a deque with a value pushed to the front of it 
   
   def test_peekfront_pushback_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.peek_front()
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests that the peek front function does not change the contents of a deque with a value pushed to the back of it
      
   def test_peekfront_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.peek_front()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))  
      
   #tests that the peek front function does not change the contents of a deque with many values pushed to the front of it
   
   def test_peekfront_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.peek_front()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))  
      
   #tests that the peek front function does not change the contents of a deque with many values pushed to the back of it
   
   def test_peekfront_pushfront_deque_len(self):
      self.__deque.push_front(1)
      self.__deque.peek_front()
      self.assertEqual(1, len(self.__deque))
      
   #tests that the peek front function does not change the size of a deque with a value pushed to the front of it
   
   def test_peekfront_pushback_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.peek_front()
      self.assertEqual(1, len(self.__deque))
      
   #tests that the peek front function does not change the size of a deque with a value pushed to the back of it
   
   def test_peekfront_pushfront3_deque_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.peek_front()
      self.assertEqual(3, len(self.__deque))
      
   #tests that the peek front function does not change the size of a deque with many values pushed to the front of it 
   
   def test_peekfront_pushback3_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.peek_front()
      self.assertEqual(3, len(self.__deque))
      
   #tests that the peek front function does not change the size of a deque with many values pushed to the back of it 
   #________________________________________________________________________________________________
   
   #_________PEEK BACK TESTS_____________
      
   def test_peekback_pushfront_deque_return(self):
      self.__deque.push_front(1)
      self.assertEqual(1, self.__deque.peek_back())
      
   #tests peek back function of a deque after a value has been pushed to the front of it
   
   def test_peekback_pushback_deque_return(self):
      self.__deque.push_back(1)
      self.assertEqual(1, self.__deque.peek_back())
      
   #tests peek back function of a deque after a value has been pushed to the back of it 
   
   def test_peekback_pushfront3_deque_return(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.assertEqual(3, self.__deque.peek_back())
      
   #tests if peek back returns value from the front of a deque after many values have been pushed to the front of it
   
   def test_peekback_pushback3_deque_return(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.assertEqual(3, self.__deque.peek_back())
      
   #tests if peek back returns value from the front of a deque after many values have been pushed to the back of it 
   
   def test_peekback_pushfront_deque_str(self):
      self.__deque.push_front(1)
      self.__deque.peek_back()
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests that the peek back function does not change the contents of a deque with a value pushed to the front of it 
   
   def test_peekback_pushback_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.peek_back()
      self.assertEqual('[ 1 ]', str(self.__deque))
      
   #tests that the peek back function does not change the contents of a deque with a value pushed to the back of it
      
   def test_peekback_pushfront3_deque_str(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.peek_back()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))  
      
   #tests that the peek back function does not change the contents of a deque with many values pushed to the front of it
   
   def test_peekback_pushback3_deque_str(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.peek_back()
      self.assertEqual('[ 1, 2, 3 ]', str(self.__deque))  
      
   #tests that the peek back function does not change the contents of a deque with many values pushed to the back of it
   
   def test_peekback_pushfront_deque_len(self):
      self.__deque.push_front(1)
      self.__deque.peek_back()
      self.assertEqual(1, len(self.__deque))
      
   #tests that the peek back function does not change the size of a deque with a value pushed to the front of it
   
   def test_peekback_pushback_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.peek_back()
      self.assertEqual(1, len(self.__deque))
      
   #tests that the peek back function does not change the size of a deque with a value pushed to the back of it
   
   def test_peekback_pushfront3_deque_len(self):
      self.__deque.push_front(3)
      self.__deque.push_front(2)
      self.__deque.push_front(1)
      self.__deque.peek_front()
      self.assertEqual(3, len(self.__deque))
      
   #tests that the peek back function does not change the size of a deque with many values pushed to the front of it 
   
   def test_peekback_pushback3_deque_len(self):
      self.__deque.push_back(1)
      self.__deque.push_back(2)
      self.__deque.push_back(3)
      self.__deque.peek_front()
      self.assertEqual(3, len(self.__deque))
      
   #tests that the peek back function does not change the size of a deque with many values pushed to the back of it 
   #________________________________________________________________________________________________  
  
  # TODO add your test methods here. Like Linked_List_Test.py,
  # each test should be in a method whose name begins with test_

if __name__ == '__main__':
   unittest.main()

  

