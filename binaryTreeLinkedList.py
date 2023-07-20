from requests import post


class BinaryTreeLinkedList:
    def __init__(self, data):
        self.data = data
        self.right_node = None
        self.left_node = None


binaryTree = BinaryTreeLinkedList("Drinks")
left_child = BinaryTreeLinkedList("Hot")
right_child = BinaryTreeLinkedList("Cold")

binaryTree.left_node = left_child
binaryTree.right_node = right_child


def preOrderTraversal(treenode):
    if not treenode:
        return
    print(treenode.data)
    preOrderTraversal(treenode.left_node)
    preOrderTraversal(treenode.right_node)


preOrderTraversal(binaryTree)


def inOrderTraversal(treenode):
    if not treenode:
        return
    inOrderTraversal(treenode.left_node)
    print(treenode.data)
    inOrderTraversal(treenode.right_node)


inOrderTraversal(binaryTree)


def postOrderTraversal(treenode):
    if not treenode:
        return
    
    postOrderTraversal(treenode.left_node)
    postOrderTraversal(treenode.right_node)
    print(treenode.data)


postOrderTraversal(binaryTree)
