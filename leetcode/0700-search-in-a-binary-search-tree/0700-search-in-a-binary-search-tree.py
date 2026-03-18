# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        stack=[root]

        while stack:
            curr=stack.pop()
            if not curr:
                return None
            if curr.val==val:
                return curr
            elif curr.val < val:
                stack.append(curr.right)
            else:
                stack.append(curr.left)
        return None

        # def helper(node,val):
        #     if not node:
        #         return None
        #     if node.val == val:
        #         return node
        #     elif node.val < val:
        #         return helper(node.right,val)
        #     else:
        #         return helper(node.left,val)
        # return helper(root,val)