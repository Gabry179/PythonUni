from BinaryTree import BinaryTree

class BinaryTreeSearch(BinaryTree):
    def __init__(self, root):
        super().__init__(root)
        self.BinaryTree_Search = self.getTree()

    def tree_search(self, node_current, node_target):
        if not node_current:
            return node_current
        if node_current == node_target:
            return node_current
        if node_target < node_current:
            return self.tree_search(self.BinaryTree_Search[node_current]['left'], node_target)
        else:
            return self.tree_search(self.BinaryTree_Search[node_current]['right'], node_target)
        
    def iterative_tree_search(self, node_current, node_target):
        while node_current and node_current != node_target:
            if node_target < node_current:
                node_current = self.tree[node_current]['left']
            else:
                node_current = self.tree[node_current]['right']
        return node_current
    
    def tree_min(self, root):
        while self.tree[root]['left'] is not None:
            root = self.tree[root]['left']
        return root
    
    def tree_max(self, root):
        while self.tree[root]['right'] is not None:
            root = self.tree[root]['right']
        return root

def main():
    BinaryTree_Search = BinaryTreeSearch(root="6")
    BinaryTree_Search.add_child('6', '5', 'left')
    BinaryTree_Search.add_child('6', '7', 'right')
    BinaryTree_Search.add_child('5', '4', 'left')
    print(BinaryTree_Search.getTree())
    print(BinaryTree_Search.tree_search('6', '4'))
    print("Iterative binary search: " + str(BinaryTree_Search.iterative_tree_search('6', '4')))
    print("Tree min: " + str(BinaryTree_Search.tree_min('6')))
    print("Tree max: " + str(BinaryTree_Search.tree_max('6')))


if __name__ == "__main__":
    main()
