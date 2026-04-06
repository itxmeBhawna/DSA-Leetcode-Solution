# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        left_side = self.inorderTraversal(root.left)
        me = [root.val]
        right_side = self.inorderTraversal(root.right)
        return left_side + me + right_side        

        