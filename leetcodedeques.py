# class RecentCounter:

#     def __init__(self):
        

#     def ping(self, t: int) -> int:
#         '''
#         initialize an empty deque 'q'
#         append the input 't' to the the deque 'q'

#             while the first element in 'q' is less than t -3000:
#                 remove the first element in q
#                 return the length of q

#         '''

from collections import deque

class RecentCounter:

    def __init__(self):
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Append the new request to the deque
        self.requests.append(t)

        # Remove all requests made before 3000 milliseconds from the current request time
        while self.requests[0] < t - 3000:
            self.requests.popleft()

        # Return the number of requests made in the last 3000 milliseconds
        return len(self.requests)

rc = RecentCounter()
print(rc.ping(1))    # Output: 1
print(rc.ping(100))  # Output: 2
print(rc.ping(3001)) # Output: 3
print(rc.ping(3002)) # Output: 3





# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

'''
The size of the deque at any point represents 
the number of requests made in the last 
3000 milliseconds.
'''