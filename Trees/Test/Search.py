from Tree import BinaryTree

class BinaryTreeSearch(BinaryTree):
    def __init__(self, root):
        super().__init__(root)
        self.tree = self.get_tree

    def tree_search(self, node_current, node_target):
        if not node_current:
            return node_current
        if node_current == node_target:
            return node_current
        if node_target < node_current:
            return self.tree_search(self.tree[node_current]['left'], node_target)
        else:
            return self.tree_search(self.tree[node_current]['right'], node_target)

    def tree_min(self, root):
        while self.tree[root]['left'] is not None:
            root = self.tree[root]['left']
        return root
    
    def tree_max(self, root):
        while self.tree[root]['right'] is not None:
            root = self.tree[root]['right']
        return root

def main():
    tree = BinaryTreeSearch(root="6")
    tree.add_child('6', '5', 'left')
    tree.add_child('6', '7', 'right')
    tree.add_child('5', '4', 'left')
    print(tree.tree_search('6', '4'))
    print("Tree min: " + str(tree.tree_min('6')))
    print("Tree max: " + str(tree.tree_max('6')))

if __name__ == "__main__":
    main()