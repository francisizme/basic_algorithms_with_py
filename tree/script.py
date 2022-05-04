class TreeNode:
    def __init__(self, text):
        self.text = text
        self.children = []

    def add_child(self, node):
        if node not in self.children:
            self.children.append(node)
        print(f"Added {node.text} to {self.text}")

    def remove_child(self, node):
        self.children = [child for child in self.children if child is not node]
        print(f"Removed {node.text} from {self.text}")

    def traverse(self):
        nodes = [self]
        while nodes:
            node = nodes.pop()
            print(node.text)
            nodes += node.children
