# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def compare_node(node, small_val = -sys.maxsize - 1, large_val = sys.maxsize):
            if not node:
                return True
            if small_val >= node.val or node.val >= large_val:
                return False
            return compare_node(node.left, small_val, node.val) and compare_node(node.right, node.val, large_val) 
            
        return compare_node(root)