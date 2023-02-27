from typing import List
from random import randint


class BSTNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def get_successor(self) -> 'BSTNode':
        if self.right:
            node = self.right
            while node.left:
                node = node.left
            return node
        else:
            node = self
            while node.parent and node == node.parent.right:
                node = node.parent
            return node.parent

    def get_predecessor(self) -> 'BSTNode':
        if self.left:
            node = self.left
            while node.right:
                node = node.right
            return node
        else:
            node = self
            while node.parent and node == node.parent.left:
                node = node.parent
            return node.parent
            

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def add(self, value: int):
        def add(tree_node: BSTNode, value: int) -> None:
            if value < tree_node.value:
                if tree_node.left is None:
                    tree_node.left = BSTNode(value)
                    tree_node.left.parent = tree_node
                else:
                    add(tree_node.left, value)
            else:
                if tree_node.right is None:
                    tree_node.right = BSTNode(value)
                    tree_node.right.parent = tree_node
                else:
                    add(tree_node.right, value)

        if self.root is None:
            self.root = BSTNode(value)
        else:
            add(self.root, value)

    def remove(self, value: int):
        raise NotImplementedError

    def inorder_traversal(self) -> List[int]:
        values = []

        def inorder_traversal(node: BSTNode):
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
    
    print('Predecessor of root:', tree.root.get_predecessor().value)
    print('Successor of root:', tree.root.get_successor().value)


if __name__ == '__main__':
    main()