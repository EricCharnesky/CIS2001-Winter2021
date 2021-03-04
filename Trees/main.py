class NTree:

    def __init__(self, value, parent=None):
        self.value = value
        self.children = []
        self.parent = parent

    def add_child(self, value):
        child = NTree(value, self)
        self.children.append(child)
        return child

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
        return max(child.height() for child in self.children)

    def is_leaf(self):
        return len(self.children) == 0


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

print( root.height() )
