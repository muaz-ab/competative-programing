# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        count = {}
        def freq(root):
            nonlocal count
            if not root:
                return 
            if root.val not in count:
                count[root.val] = 1
            elif root.val in count:
                count[root.val] += 1
            root.left = freq(root.left)
            root.right = freq(root.right)
            return
        freq(root)
        maxx = max(count.values())
        return [i for i , j in count.items() if j == maxx]
