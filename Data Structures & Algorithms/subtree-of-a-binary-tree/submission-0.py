from collections import deque
from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)
            return False

        if not subRoot:
            return True
        if not root:
            return False

        q = deque([root])
        while q:
            node = q.popleft()
            if sameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        return False