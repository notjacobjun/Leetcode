# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Observ:
- For the left subtree we know that every value in that subtree is def less than the current node, so use the search property to our advantage here
- Need to know how many nodes are in a subtree so we can decide whether or not the kth smallest node is in that subtree or not

Count # of nodes in current tree:
- Keep track of # of nodes in the left and right subtree 
    - Using simple DFS or BFS
- For each node know that we have the nth smallest nodes then if we need to move left or right
- recursively iterate through the tree on each decision until our current node is the node we want based on the counts
- Maybe create a hash table with the left_count and right_count for each node in the tree once performing a single DFS
    - So we don't do extra work than necessary

In order traversal:
- K.I. In order traversal gives us the sorted order of the BST 
- Simply just iterate using in order traversal until we reach the kth iteration.
"""


class Solution:
    def helper(self, node):
        # base case
        if node is None:
            return

        # recursive cases
        if node.left is not None:
            self.helper(node.left)

        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return

        if node.right is not None:
            self.helper(node.right)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.res = 0

        self.helper(root)
        return self.res
