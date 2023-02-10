# recursion: a function that calls itself
# iteration: loops

# countdown
# take in a numbeer
# print from that number fown to 0
# print blastoff
# we can assume only positive numbers will be in here

# 1. for loop
# 2. while loop
# 3. recursion

def countdown_for(n):
    for i in range(n, 0, -1):
        print(i)
    print('blast off!')
countdown_for(5)

def countdown_while(n):
    i = n
    while i > 0:
        print(i)
        i -= 1
    print('blast off!')
     
# psuedocode out the def of a while loop
# start by defining the base case (aska the condition that ends your while loop)
# do the inside of the loop
# end with the final element

# countdown_while(5)

def countdown_recursion(n):
    # figure out the base case
    if n == 0: # constant time
        print('blast off!') # constant time
        return
    else:
        print(n)
        countdown_recursion(n -1) # O(n) for countdown_recursion
        
        # runtime O(n)
print('here')
# n = 5  open
# n = 4  open
# n = 3  open
# n = 2  open
# n = 1  open (still running) after the end, they close backwards
# n = 0  closes, function has ended



# 5
# 4
# 3
# 2
# 1
# blast off!
countdown_recursion(5)



