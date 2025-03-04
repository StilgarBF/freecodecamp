class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BinarySearchTree:
    """
    BinarySearchTree class implements a binary search tree (BST) with methods to insert, search, delete, and traverse nodes.
    A binary search tree (BST) is a node-based binary tree data structure which has the following properties:
    - The left subtree of a node contains only nodes with keys less than the node's key.
    - The right subtree of a node contains only nodes with keys greater than the node's key.
    - Both the left and right subtrees must also be binary search trees.

    Practical use cases of binary search trees:
    - Searching: BSTs provide efficient searching capabilities with an average time complexity of O(log n).
    - Sorting: Inorder traversal of a BST gives a sorted sequence of elements.
    - Dynamic Set Operations: BSTs support insertion and deletion operations, making them suitable for applications where data is constantly changing.
    - Implementing associative arrays: BSTs can be used to implement map and set data structures.
    - Priority Queues: BSTs can be used to implement priority queues where elements are dequeued in a specific order.
    - Database Indexing: BSTs are used in databases to index data for quick retrieval.

    Benefits of binary search trees:
    - Efficient searching, insertion, and deletion operations.
    - Maintains a sorted order of elements.
    - Flexible and can be balanced to ensure optimal performance.
    """
    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:

            node.right = self._insert(node.right, key)
        return node

    def insert(self, key):
        self.root = self._insert(self.root, key)
        
    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)
    
    def search(self, key):
        return self._search(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key) 
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left   
            
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)   
        
        return node

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _min_value(self, node):
        while node.left is not None:
            node = node.left
        return node.key

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)

    def inorder_traversal(self):
        result = []
        self._inorder_traversal(self.root, result)
        return result
    # 2 additional methods to print the tree
    # Helper function to print the tree
    def _print_tree(self, node, level=0, prefix="Root: "):
        if node is not None:
            print(" " * (level * 4) + prefix + str(node.key))
            if node.left is not None or node.right is not None:
                if node.left:
                    self._print_tree(node.left, level + 1, "L--- ")
                else:
                    print(" " * ((level + 1) * 4) + "L--- None")
                if node.right:
                    self._print_tree(node.right, level + 1, "R--- ")
                else:
                    print(" " * ((level + 1) * 4) + "R--- None")
    # 'public' method to print the tree
    def print_tree(self):
        self._print_tree(self.root)

bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80, 110, 90, 10, 15, 25, 35, 45, 55, 65, 75, 85, 95]

for node in nodes:
    bst.insert(node)
bst.print_tree()
print('Search for 80:', bst.search(80))

print("Inorder traversal:", bst.inorder_traversal())

bst.delete(40)
bst.print_tree()
print("Search for 40:", bst.search(40))
print('Inorder traversal after deleting 40:', bst.inorder_traversal())