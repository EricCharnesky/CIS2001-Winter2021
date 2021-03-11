class BinaryTree:

    class Position:

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def data(self):
            return self._node.data

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)


    class Node:

        def __init__(self, data, parent=None, left_child=None, right_child=None):
            self.parent = parent
            self.left_child = left_child
            self.right_child = right_child
            self.data = data

    def _make_position(self, node):
        if node is None:
            return None
        return self.Position(self, node)

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position._container is not self:
            raise ValueError()

        return position._node


    def __init__(self, data):
        self._root = self.Node(data)

    def root(self):
        return self._make_position(self._root)

    def add_left(self, position, data):
        node = self._validate(position)
        if node.left_child is not None:
            raise ValueError("Left child already exists")

        node.left_child = self.Node(data, node)
        return self._make_position(node.left_child)

    def add_right(self, position, data):
        node = self._validate(position)
        if node.right_child is not None:
            raise ValueError("right child already exists")

        node.right_child = self.Node(data, node)
        return self._make_position(node.right_child)

    def left(self, position):
        node = self._validate(position)
        return self._make_position(node.left_child)

    def right(self, position):
        node = self._validate(position)
        return self._make_position(node.right_child)

    def parent(self, position):
        node = self._validate(position)
        return self._make_position(node.parent)

    def depth(self, position):
        node = self._validate(position)
        current_depth = 0
        current_parent = node.parent
        while current_parent is not None:
            current_depth += 1
            current_parent = current_parent.parent
        return current_depth

    def children(self, position):
        node = self._validate(position)
        if node.left_child is not None:
            yield self._make_position(node.left_child)
        if node.right_child is not None:
            yield self._make_position(node.right_child)

    def height(self, position=None):
        if position is None:
            position = self.root()
        if self.is_leaf(position):
            return self.depth(position)
        return max(self.height(child) for child in self.children(position))

    def is_leaf(self, position):
        node = self._validate(position)
        return node.left_child is None and node.right_child is None

    def is_empty(self):
        return self._root is None

    def preorder(self):
        if not self.is_empty():
            for position in self._subtree_preorder(self.root()):
                yield position

    def _subtree_preorder(self, position):
        yield position
        for child in self.children(position):
            for subtree_position in self._subtree_preorder(child):
                yield subtree_position

    def inorder(self):
        if not self.is_empty():
            for position in self._subtree_inorder(self.root()):
                yield position

    def _subtree_inorder(self, position):
        if self.left(position) is not None:
            for subtree_position in self._subtree_inorder(self.left(position)):
                yield subtree_position
        yield position
        if self.right(position) is not None:
            for subtree_position in self._subtree_inorder(self.right(position)):
                yield subtree_position


class BinarySearchTree(BinaryTree):

    def add(self, data):
        if data < self._root.data:
            self.add_left(self.root(), data)
        elif data > self._root.data:
            self.add_right(self.root(), data)

    def add_left(self, position, data):
        node = self._validate(position)
        if node.left_child is None:
            return super().add_left(position, data)
        else:
            left_child = node.left_child
            if data < left_child.data:
                self.add_left(self.left(position), data)
            elif data > left_child.data:
                self.add_right(self.left(position), data)

    def add_right(self, position, data):
        node = self._validate(position)
        if node.right_child is None:
            return super().add_right(position, data)
        else:
            right_child = node.right_child
            if data < right_child.data:
                self.add_left(self.right(position), data)
            elif data > right_child.data:
                self.add_right(self.right(position), data)


binary_tree = BinaryTree(10)

root = binary_tree.root()

left_child = binary_tree.add_left(root, 5)
right_child = binary_tree.add_right(root, 15)

binary_tree.add_left(left_child, 1)

binary_tree.add_right(right_child, 100)

print(binary_tree.height())

print('pre order')
for position in binary_tree.preorder():
    print(position.data())

print('in order')
for position in binary_tree.inorder():
    print(position.data())



bst = BinarySearchTree(10)
bst.add(5)
bst.add(20)
bst.add(15)
bst.add(30)
bst.add(1)
bst.add(7)
bst.add(9)


print('in order')
for position in bst.inorder():
    print(position.data())