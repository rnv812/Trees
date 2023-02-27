from binary_tree import BinaryTree, BinaryTreeNode


def is_full_binary_tree(root: BinaryTreeNode) -> bool:
    if root is None:
        return True

    if root.left is None and root.right is None:
        return True

    if root.left is not None and root.right is not None:
        return (is_full_binary_tree(root.left) and is_full_binary_tree(root.right))

    return False


def main():
    tree = BinaryTree()
    
    tree.root = BinaryTreeNode(1)
    print(is_full_binary_tree(tree.root))
    
    tree.root.left = BinaryTreeNode(2)
    print(is_full_binary_tree(tree.root))
    
    tree.root.right = BinaryTreeNode(3)
    print(is_full_binary_tree(tree.root))

    tree.root.right.left = BinaryTreeNode(4)
    tree.root.right.right = BinaryTreeNode(5)
    print(is_full_binary_tree(tree.root))


if __name__ == '__main__':
    main()