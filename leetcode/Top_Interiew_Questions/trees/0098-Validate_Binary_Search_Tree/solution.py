from typing import Optional


# Definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, minimum, maximum):
            if not node:
                return True

            if not minimum < node.val < maximum:
                return False

            return validate(node.left, minimum, node.val) and validate(
                node.right, node.val, maximum
            )

        return validate(root, float("-inf"), float("inf"))
