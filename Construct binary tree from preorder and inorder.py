"""
You did this with some help to come up with the algorithm but the coding was done yourself 5/10
Observations:
- The main problem is that there null nodes are indicated for
- Significant part of this problem is also finding out that placement of the nodes in the tree specifically, b/c finding the # of nodes in each side of the tree is only so helpful, but we need to specifically find the placement.
- In order traversal gets the leftmost nodes first then gets the root of the current leftmost and the right child of the root
    inorder(root.left)
    print(root)
    inorder(root.right)
- Pre order: Gets the root element first, then it recursively calls pre order on the left child, then recursively call on the right child
    print(root)
    preorder(root.left)
    preorder(root.right)

- Might help to find the total number of nodes in the left side of the tree and the right side of the tree for each tree (including subtrees) in the overall tree structure.
- Once we have to total number of nodes in each side then we can deduce where null nodes are appropriate. Also need to figure out the location of each of these nodes
- Finding out the # of nodes on each side of the tree can help us to find out where the nodes are since we are using both traversal methods.
- Notice that inorder trav iterates through all the nodes in a minor diagonal fashion. (from bottom left to top right)
- While preorder goes from the top to the left then moves to the whatever is remaining on the right

KEY INSIGHTS:
- The first node in pre-order traveral is going to be the root of the tree.
- Then since we know which node the root is, every node to the left of the root in the inorder traveral list is going to be in the left subtree of the root and every value to the root of the root is going to be in the right subtree!

Approach 1:
- Find the number of nodes on the left side of the root tree
- Then find # of nodes on the right side of root tree.
- Continue this process recursively until we reach each node

Example:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
"""
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode()
        self.helper(preorder, inorder, root)
        return root

    def helper(self, preorder, inorder, node):
        """
        Constructs the remaining list based on the split found from preorder and inorder list recursively

        Returns:
        A node constructed from the current recursive iteration
        """
        # base case
        if not preorder or not inorder or node == None:
            return

        # Find the root of the current tree by picking from preorder list
        node.val = preorder.pop(0)

        # recursive case (partition both lists into the left and right subtree based on the position of root in the inorder list)
        # find the position of root in the inorder list
        idx = inorder.index(node.val)
        # split the left subtree
        node.left, node.right = TreeNode(), TreeNode()
        if not inorder[:idx]:
            node.left = None
        if not inorder[idx+1:]:
            node.right = None
        self.helper(preorder, inorder[:idx], node.left)
        # split the right subtree
        self.helper(preorder, inorder[idx+1:], node.right)
