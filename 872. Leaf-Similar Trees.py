def leafSimilar(root1, root2):
    def find_leaf(root, elem):
        if root is None:
            return
        if root.left is None and root.right is None:
            elem.append(root.val)
        find_leaf(root.left, elem)
        find_leaf(root.right, elem)
        return elem

    return find_leaf(root1, []) == find_leaf(root2, [])
