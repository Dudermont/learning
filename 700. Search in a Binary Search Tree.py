def searchBST(self, root, val):
    if root is None or root.val == val:
        return root
    if root.val > val:
        return self.searchBST(root.left, val)
    else:
        return self.searchBST(root.right, val)
