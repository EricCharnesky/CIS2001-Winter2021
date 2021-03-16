class NTree:

    class Position:

        def __init__(self, container, tree):
            self._container = container
            self._tree = tree

        def data(self):
            return self._tree.value

        def __eq__(self, other):
            return type(other) is type(self) and other._tree is self._tree

        def __ne__(self, other):
            return not (self == other)

    def _validate(self, position):
        if not isinstance(position, self.Position):
            raise TypeError()
        if position._container is not self.root()._tree:
            raise ValueError()

        return position._tree

    def __init__(self, value, parent=None):
        self.value = value
        self._children = []
        self.parent = parent

    def root(self):
        if self.is_empty():
            return None

        current = self

        while current.parent is not None:
            current = current.parent

        return self.Position(current, current)

    def is_root(self, position):
        return position == self.root()

    def parent(self, position):
        current_tree = self._validate(position)
        return self.Position( self.root()._tree, current_tree.parent )

    def is_leaf(self, position):
        current_tree = self._validate(position)
        return current_tree.is_leaf()

    def is_empty(self):
        return self.value is None and len(self._children) == 0

    def add_child(self, value):
        child = NTree(value, self)
        self._children.append(child)
        return child

    def number_of_children(self, position):
        current_tree = self._validate(position)
        return len(current_tree._children)

    def children(self, position):
        current_tree = self._validate(position)
        for child in current_tree._children:
            yield self.Position(self.root()._tree, child)

    def positions(self):
        for subtree in self._subtree_preorder(self.root()):
            yield subtree

    def _subtree_preorder(self, position):
        yield position
        for child in self.children(position):
            for sub_tree in self._subtree_preorder(child):
                yield sub_tree

    def __str__(self):
        return self.value

    def depth(self):
        current_depth = 0
        current_parent = self.parent
        while current_parent is not None:
            current_depth += 1
            current_parent = current_parent.parent
        return current_depth

    def height(self):
        if self.is_leaf():
            return self.depth()
        return max(child.height() for child in self._children)

    def is_leaf(self):
        return len(self._children) == 0

    def breadthfirst(self):
        # this is a bad queue but it's ok for now
        queue = [self.root()]
        while len(queue) != 0:
            current_position = queue.pop(0) # bad implementation of dequeue
            yield current_position
            for child in self.children(current_position):
                queue.append(child)


root = NTree('CIS2001-Winter2021')
print("root.depth(): " + str(root.depth()))
lab1 = root.add_child('Lab1')
print("lab1.depth(): " + str(lab1.depth()))
lab1py = lab1.add_child('lab1.py')
print("lab1py.depth(): " + str(lab1py.depth()))
project1 = root.add_child('Project 1')
project1.add_child('MazeSolver.py')
project1.add_child('main.py')
project1.add_child('unit_test.py')
root.add_child('hello_world.py')

#print( root.height() )


root_position = root.root()

#print(root.number_of_children(root_position))

#for child in root.children(root_position):
    #print(child.data())


#for position in root.positions():
    #print(position.data())

print(' bread first traversal - level by level')
for position in root.breadthfirst():
    print(position.data())