from typing import List
from random import randint


class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def add(self, value: int):
        def add(tree_node: Node, value: int) -> None:
            if value < tree_node.value:
                if tree_node.left is None:
                    tree_node.left = Node(value)
                else:
                    add(tree_node.left, value)
            else:
                if tree_node.right is None:
                    tree_node.right = Node(value)
                else:
                    add(tree_node.right, value)

        if self.root is None:
            self.root = Node(value)
        else:
            add(self.root, value)

    def remove(self, value: int):
        raise NotImplementedError

    def inorder_traversal(self) -> List[int]:
        values = []

        def inorder_traversal(node: Node):
            if node is None:
                return
            inorder_traversal(node.left)
            values.append(node.value)
            inorder_traversal(node.right)

        inorder_traversal(self.root)

        return values


def main():
    tree = BinarySearchTree()
    values = [randint(-10, 10) for _ in range(20)]

    for value in values:
        tree.add(value)

    print('Original values:', values)
    print('In order traversal:', tree.inorder_traversal())


if __name__ == '__main__':
    main()