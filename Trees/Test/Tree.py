class BinaryTree():
    def __init__(self, root):
        self.tree = dict()
        self.add_root(root)

    def add_root(self, root):
        self.tree[root] = {"parent":None, "left":None, "right":None}

    def add_child(self, parent, node_name, side):
        if parent in self.tree and not self.tree[parent][side]:
            self.tree[parent][side] = node_name
            self.tree[node_name] = {"parent":parent, "left":None, "right":None}

    def is_root(self, node_name):
        if not self.tree[node_name]["parent"]:
            return True
        return False
    
    def get_tree(self):
        return self.tree

    def is_leaf(self, node_name):
        return not self.tree[node_name]["left"] and not self.tree[node_name]["right"]

    def get_children(self, node_name):
        children = list()
        if self.tree[node_name]["left"]:
            children.append(self.tree[node_name]["right"])
        if self.tree[node_name]["right"]:
            children.append(self.tree[node_name]["left"])
        return children
        
    def depth(self, node_name):
        if self.is_root(node_name):
            return 1
        return 1 + self.depth(self.tree[node_name]["parent"])
    
    def height(self, node_name):
        if self.is_leaf(node_name):
            return 0
        return 1 + max(self.height(child) for child in self.get_children(node_name))

def main():
    tree = BinaryTree('root')
    tree.add_child('root','node1','left')
    tree.add_child('root','node2','right')
    print(tree.get_tree())
    print(tree.is_root("root"))
    print(tree.is_leaf("node1"))
    print(tree.get_children("root"))
    print(tree.depth("node1"))
    print(tree.height("root"))

if __name__ == "__main__":
    main()