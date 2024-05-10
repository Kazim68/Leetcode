# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = []
        if not root: return 0

        def helper(node, score):
            if not node: return
            elif not node.left and not node.right:
                res.append(score*10+node.val)
                return
            else:
                helper(node.left, score*10+node.val)
                helper(node.right, score*10+node.val)
        
        helper(root, 0)
        return sum(res)