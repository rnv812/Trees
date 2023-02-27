from binary_tree import BinaryTree, BinaryTreeNode


def count_nodes(root: BinaryTreeNode) -> int:
    if root is None:
        return 0
    
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def _is_complete_binary_tree(root: BinaryTreeNode, index: int, nodes_count: int) -> bool:
    if root is None:
        return True
    
    if index >= nodes_count :
        return False

    return (
        _is_complete_binary_tree(root.left , 2 * index + 1, nodes_count) and
        _is_complete_binary_tree(root.right, 2 * index + 2, nodes_count)
    )


def is_complete_binary_tree(root: BinaryTreeNode) -> bool:
    return _is_complete_binary_tree(root, 0, count_nodes(root))


def main():
    tree = BinaryTree()
    
    tree.root = BinaryTreeNode(1)
    print(is_complete_binary_tree(tree.root))
    
    tree.root.left = BinaryTreeNode(2)
    print(is_complete_binary_tree(tree.root))
    
    tree.root.right = BinaryTreeNode(3)
    print(is_complete_binary_tree(tree.root))

    tree.root.right.left = BinaryTreeNode(4)
    tree.root.right.right = BinaryTreeNode(5)
    print(is_complete_binary_tree(tree.root))

    tree.root.left.left = BinaryTreeNode(6)
    tree.root.left.right = BinaryTreeNode(7)
    print(is_complete_binary_tree(tree.root))


if __name__ == '__main__':
    main()