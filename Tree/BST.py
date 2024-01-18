class Node:
    def __init__(self, item=None, left=None, right=None) -> None:
        self.item = item
        self.left = left
        self.right = right


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        self.root = self.rinsert(self.root, data)

    def rinsert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.item:
            root.left = self.rinsert(root.left)
        elif data > root.item:
            root.right = self.rinsert(root.right, data)
        return root

    def search(self, data):
        return self.rsearch(self.root, data)

    def rsearch(self, root, data):
        if root == None or root.item == data:  # not a tree root, public variable here
            return root
        if data < root.item:
            return self.rsearch(root.left, data)
        else:
            return self.rsearch(root.right, data)

    def inorder(self):
        result = list()
        self.rinorder(self.root, result)
        return result

    def inorder(self, root, result):
        if root:
            self.rinorder(root.left, result)
            result.append(root.item)
            self.rinorder(root.right, result)

    def preorder(self):
        result = list()
        self.preorder(self.root, result)
        return result

    def preorder(self, root, result):
        if root:
            result.append(root.item)
            self.preorder(root.left, result)
            self.preorder(root.right, result)

    def postorder(self):
        result = list()
        self.rpostorder(self.root, result)
        return result

    def rpostorder(self, root, result):
        if root:
            self.rpostorder(root.left, result)
            self.rpostorder(root.right, result)
            result.append(root.item)

    def min_value(self, temp):
        current = temp
        while current.left is not None:
            current = current.left
        return current.item

    def max_value(self, temp):
        current = temp
        while current.right is not None:
            current = current.right
        return current.item

    def delete(self, data):
        self.root = self.rdelete(self.root, data)

    def rdelete(self, root, data):
        if root is None:
            return root
        if data < root.item:
            root.left = self.rdelete(root.left, data)
        elif data > root.item:
            root.right = self.rdelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.item = self.min_value(root.right)  # replacing with successer
            self.rdelete(root.right, root.item)
        return root

    def size(self):
        return len(self.inorder())
