from typing import List, Optional
from random import randint
from binary_tree import BinaryTreeNode, BinaryTree


class BSTNode(BinaryTreeNode):
    def __init__(self, value: int) -> None:
        super().__init__(value)
        self.parent = None

    def __str__(self) -> str:
        return f'{self.value}'

    def get_successor(self) -> Optional['BSTNode']:
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

    def get_predecessor(self) -> Optional['BSTNode']:
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


class BinarySearchTree(BinaryTree):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def _find_node(node: BSTNode, value: int) -> Optional[BSTNode]:
        while node is not None:
            if value < node.value:
                node = node.left
            elif value > node.value:
                node = node.right
            else:
                return node
        return None

    @staticmethod
    def _add(node: BSTNode, value: int) -> None:
        if value < node.value:
            if node.left is None:
                node.left = BSTNode(value)
                node.left.parent = node
            else:
                BinarySearchTree._add(node.left, value)
        else:
            if node.right is None:
                node.right = BSTNode(value)
                node.right.parent = node
            else:
                BinarySearchTree._add(node.right, value)

    @staticmethod
    def _remove(tree: 'BinarySearchTree', subtree: BSTNode, value: int) -> bool:
        node = BinarySearchTree._find_node(subtree, value)
        if node is None:
            return False

        if node.left is None or node.right is None:
            child = node.left or node.right
            if node.parent is None:
                if child is not None:
                    child.parent = None
                tree.root = child
            else:
                if node == node.parent.left:
                    node.parent.left = child
                else:
                    node.parent.right = child
                if child is not None:
                    child.parent = node.parent
        else:
            successor = node.get_successor()
            node.value = successor.value
            BinarySearchTree._remove(tree, node.right, successor.value)
        return True

    @staticmethod
    def _inorder_traversal(node: BSTNode):
        if node:
            yield from BinarySearchTree._inorder_traversal(node.left)
            yield node.value
            yield from BinarySearchTree._inorder_traversal(node.right)

    def add(self, value: int) -> None:
        if self.root is None:
            self.root = BSTNode(value)
        else:
            BinarySearchTree._add(self.root, value)

    def get(self, value: int) -> Optional[int]:
        node = BinarySearchTree._find_node(self.root, value)
        if node is None:
            return None
        return node.value

    def remove(self, value: int) -> bool:
        if self.root is None:
            return False
        return self._remove(self, self.root, value)

    def min(self) -> int:
        node = self.root
        while node.left:
            node = node.left
        return node.value

    def max(self) -> int:
        node = self.root
        while node.right:
            node = node.right
        return node.value

    def inorder_traversal(self) -> List[int]:
        return list(BinarySearchTree._inorder_traversal(self.root))


def main():
    tree = BinarySearchTree()
    values = [randint(-10, 10) for _ in range(2)]
    print('Random values:', values)

    for value in values:
        tree.add(value)
        print(f'After adding {value} to tree: ', tree.inorder_traversal())

    print('Predecessor of root:', tree.root.get_predecessor())
    print('Successor of root:', tree.root.get_successor())

    print('Min:', tree.min())
    print('Max:', tree.max())

    for value in values:
        tree.remove(value)
        print(f'After removing {value} from tree: ', tree.inorder_traversal())


if __name__ == '__main__':
    main()
