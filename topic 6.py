class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print(" " * level * 2 + self.name)
        for child in self.children:
            child.display(level + 1)

# Example Usage
root = TreeNode("Orders")
category_a = TreeNode("Category A")
category_b = TreeNode("Category B")
order_a1 = TreeNode("Order A1")
order_a2 = TreeNode("Order A2")
order_b1 = TreeNode("Order B1")

category_a.add_child(order_a1)
category_a.add_child(order_a2)
category_b.add_child(order_b1)
root.add_child(category_a)
root.add_child(category_b)

root.display()
