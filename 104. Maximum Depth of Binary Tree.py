def maxDepth(self, root):
    if not root:
        return 0
    maxlvl = max(self.maxDepth(root.left), self.maxDepth(root.right))
    return 1 + maxlvl
