from script import TreeNode


def dfs(root: TreeNode, target, path=()):
    path += (root,)
    if root.text == target:
        return '/'.join([node.text for node in path])

    for child in root.children:
        new_path = dfs(child, target, path)
        if new_path is not None:
            return new_path

    return None
