from collections import deque
# assume always starting from 1
# make a queue that just has 1 in it
# for loop from range(n)
    # define front number in list to examine
    # add a 0 to the end of front number  and then enqueue it
    # add a 1 to the end of front number and then enqueue it
'''
Deque (Doubly Ended Queue) in Python is implemented using
the module “collections“. Deque is preferred over a list in 
the cases where we need quicker append and pop operations 
from both the ends of the container, as deque provides 
an O(1) time complexity for append and pop operation
'''

def generate(n):
    q = deque() # 0(1)
    q.append(1)  # adds to the right side 0(1)
    for i in range(n): # O(n)
        
        current = str(q.popleft()) # O(1)
        print(current)             # O(1)
        next_num = current + '0'   # O(1)
        next_next_num = current + '1' # O(1)
        print(next_num, next_next_num) # O(1)
        q.append(next_num) # O(1)
        q.append(next_next_num) # O(1)
generate(5)