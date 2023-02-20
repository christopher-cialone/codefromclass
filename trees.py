class ListNode:
    def __init__(self, value):
        self.val = value
        self.next = None

# head = ListNode(10)
# second = ListNode(5)


# head.next = second

class BinaryTreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

root =  BinaryTreeNode(10)
root_left = BinaryTreeNode(11)
root_right = BinaryTreeNode(-3)

root.left = root.left
root.right = root.right