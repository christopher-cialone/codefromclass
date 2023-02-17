''' Linked Lists '''

class Node:
    def __init__(self, value):
        self.val = value
        self.next = next

head_node = Node(5)
second_node = Node(7)

head_node.next = second_node

# print(head_node.val, head_node.next)
# print(second_node.val, second_node.next)

node = second_node       
for i in range(5):
    new_node = Node(i) # i = 0 
    node.next = new_node
    node = node.next

# given the head node of a linked list, print out the values
# of each node i the list in order

# head_node