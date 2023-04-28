class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def test(left, right):
            if (left == None) and (right == None):
                return True
            elif (left == None) or (right == None):
                return False
            elif left.val != right.val:
                return False
            return test(left.left, right.right) and test(left.right, right.left)
        
        return test(root.left, root.right)
