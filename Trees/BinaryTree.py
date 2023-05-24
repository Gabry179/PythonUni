class BinaryTree:
    def __init__(self, root):
        self.tree = dict()
        self.add_root(root)
    
    def add_root(self, node_name):
        self.tree[node_name] = {"parent": None, "left": None, "right": None}

    def getTree(self):
        return self.tree

    def add_child(self, parent, node_name, side):
        if parent in self.tree and not self.tree[parent][side]:
            self.tree[parent][side] = node_name
            self.tree[node_name] = {"parent": parent, "left": None, "right": None}

    def get_left(self, node_name):
        return self.tree[node_name]["left"]
    
    def get_right(self, node_name):
        return self.tree[node_name]["right"]

    def get_sibling(self, node_name):
        parent = self.tree[node_name]["parent"]
        if node_name == self.tree[parent]["left"]:
            return self.tree[parent]["right"]
        else:
            return self.tree[parent]["left"]

    def get_root(self):
        for i in self.tree.keys():
            if not self.tree[i]['parent']:
                return i
        return None

    def is_root(self, node_name):
        if not node_name in self.tree:
            raise Exception("The node is not in the tree.")
        if not self.tree[node_name]["parent"]:
            return True
        return False

    def has_leaf(self, node_name):
        if not node_name in self.tree:
            raise Exception("The node is not in the tree.")
        return not self.tree[node_name]["left"] and not self.tree[node_name]["right"]
    
    def get_children(self, node_name):
        children = list()
        if self.tree[node_name]['left']:
            children.append(self.tree[node_name]['left'])
        if self.tree[node_name]['right']:
            children.append(self.tree[node_name]['right'])
        return children

    def depth(self, node_name):
        if self.is_root(node_name):
            return 1
        return 1 + self.depth(self.tree[node_name]['parent'])

    def height(self, node_name):
        if self.has_leaf(node_name):
            return 0
        return 1 + max(self.height(child) for child in self.get_children(node_name))

def main():
    tree = BinaryTree("root")
    tree.add_child("root", "nodo1", "left")
    tree.add_child("root", "nodo2", "right")
    tree.add_child("nodo1", "nodo3", "left")
    print("Tree: " + str(tree.getTree()))
    print("Left node: " + tree.get_left("root"))
    print("Right node: " + tree.get_right("root"))
    print("Sibling of nodo1: " + tree.get_sibling("nodo1"))
    print("Tree root: " + tree.get_root())
    print("Is root: " + str(tree.is_root("root")))
    print("Has leaf: " + str(tree.has_leaf("nodo1")))
    print("Children: " + str(tree.get_children("root")))
    print("Depth: " + str(tree.depth("nodo1")))
    print("Height: " + str(tree.height("nodo1")))

if __name__ == '__main__':
    main()