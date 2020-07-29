
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # solution without recursion
        cur = self
        while cur is not None:
            if cur.value > value:
                if cur.left == None:
                    cur.left = BSTNode(value)
                    return cur.left.value
                else:
                    cur = cur.left
            if cur.value <= value:
                if cur.right == None:
                    cur.right = BSTNode(value)
                    return cur.right.value
                else:
                    cur = cur.right
        # solution with recursion
        # if(self.value > value):
        #     if(self.left == None):
        #         self.left = BSTNode(value)
        #     else:
        #         self.left.insert(value)
        # if(self.value <= value):
        #     if(self.right == None):
        #         self.right = BSTNode(value)
        #     else:
        #         self.right.insert(value)


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if(self.value == target):
            return True
        if(self.value > target):
            if(self.left == None):
                return False
            if(self.left.value == target):
                return True
            else:
                return self.left.contains(target)
        if(self.value <= target):
            if(self.right == None):
                return False
            if(self.right.value == target):
                return True
            else:
                return self.right.contains(target)
    # Return the maximum value found in the tree
    def get_max(self):
        if(self.right == None):
            return self.value
        else:
            return self.right.get_max()


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if(self.right):
            self.right.for_each(fn)
        if(self.left):
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if(node.left):
            node.left.in_order_print(node.left)
        print(node.value)
        if(node.right):
            node.right.in_order_print(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = []
        queue.append(node)
        while(queue):
            current_node = queue.pop(0)
            print(current_node.value)
            if(current_node.left):
                queue.append(current_node.left)
            if(current_node.right):
                queue.append(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        print(node.value)
        if(node.left):
            node.left.dft_print(node.left)
        if(node.right):
            node.right.dft_print(node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if(node.left):
            node.left.pre_order_dft(node.left)
        if(node.right):
            node.right.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if (node.left):
            node.left.post_order_dft(node.left)
        if (node.right):
            node.right.post_order_dft(node.right)
        print(node.value)
