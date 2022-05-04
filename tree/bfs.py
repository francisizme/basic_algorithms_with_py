from collections import deque
from script import TreeNode


def bfs(tree_node: TreeNode, pattern):
    # init frontier
    frontier = deque()
    # push queue
    frontier.appendleft([tree_node])

    # loop while frontier is not empty
    while frontier:
        current_path = frontier.pop()
        # bfs runs based on Queue i.e., FIFO then current node should be the last el from the list
        current_node = current_path[-1]
        # return if current node is what we've been finding
        if current_node.text == pattern:
            return '/'.join([node.text for node in current_path])

        # otherwise, adding children to continue seeking
        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)
            frontier.appendleft(new_path)
