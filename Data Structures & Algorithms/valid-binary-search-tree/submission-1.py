# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = None
        def validInorder(root: TreeNode) -> bool:
            nonlocal prev
            if root is None:
                return True
            if not validInorder(root.left):
                return False
            if prev is not None and prev.val>=root.val:
                return False
            prev=root
            return validInorder(root.right)
        return validInorder(root)