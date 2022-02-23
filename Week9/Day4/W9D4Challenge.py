class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def get_value(self):
        return self.value

    def set_left(self, new_node):
        self.left = new_node

    def set_right(self, new_node):
        self.right = new_node

    def set_value(self, new_value):
        self.value = new_value

    def add_node(self, node):
        if node.value > self.get_value():
            if self.get_right():
                self.get_right().add_node(node)
            else:
                self.set_right(node)
        elif node.value < self.get_value():
            if self.get_left():
                self.get_left().add_node(node)
            else:
                self.set_left(node)
        else:
            print("Node with this value already added")

    def search(self, value):
        if value > self.get_value():
            if self.get_right():
                return self.get_right().search(value)
        elif value < self.get_value():
            if self.get_left():
                return self.get_left().search(value)
        elif value == self.get_value():
            return self
        else:
            return False

    def print_tree(self):
        print(f'({self.value})', end=' ')
        if self.left:
            print(f'left - {self.get_left().get_value()}', end=' ')
        if self.right:
            print(f'right - {self.get_right().get_value()}', end=' ')
        print()
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


root = Node(30)
root.add_node(Node(10))
root.add_node(Node(50))
root.add_node(Node(5))
root.add_node(Node(15))
root.add_node(Node(20))

root.print_tree()

print('******************')
(root.search(10).print_tree())
