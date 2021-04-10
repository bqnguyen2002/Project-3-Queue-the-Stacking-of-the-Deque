import sys # for sys.argv, the command-line arguments
from Stack import Stack

def delimiter_check(filename):
   # TODO replace pass with an implementation that returns True
   # if the delimiters (), [], and {} are balanced and False otherwise.
   
   #Source: https://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python
   
   delimiters = Stack()
   with open(filename) as file:
      for line in file:  
         for ch in line: 
            if(ch == '(' or ch == '[' or ch == '{'):
               delimiters.push(ch)
            if(ch == ')' or ch == ']' or ch == '}'):
               compare = delimiters.pop()
               if(compare != '(' and ch == ')'):
                  return False
               if(compare != '[' and ch == ']'):
                  return False
               if(compare != '{' and ch == '}'):
                  return False
   if len(delimiters) == 0:
      return True
   return False
   
   #first two if statements push only the open delimiters onto the stack
   #last three if statements check if incoming closing delimiters pair with the opening delimiter on the top of the stack
   #if they don't match return false and return true if all the opening delimiters on the stack have been popped

if __name__ == '__main__':
   # The list sys.argv contains everything the user typed on the command 
   # line after the word python. For example, if the user types
   # python Delimiter_Check.py file_to_check.py
   # then printing the contents of sys.argv shows
   # ['Delimiter_Check.py', 'file_to_check.py']
   print (delimiter_check('delimiter.txt'))
   if len(sys.argv) < 2:
      # This means the user did not provide the filename to check.
      # Show the correct usage.
      print('Usage: python Delimiter_Check.py file_to_check.py')
   else:
      if delimiter_check(sys.argv[1]):
         print('The file contains balanced delimiters.')
      else:
         print('The file contains IMBALANCED DELIMITERS.')


