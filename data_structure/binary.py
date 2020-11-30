class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.right)
        print(root.val)
        postorder(root.left)


r = Node(50)
# print("r:", r)
# print("rleft:", r.left)
r = insert(r, 30)
# print("r:", r)
# print("rleft:", r.left)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
# inorder(r)
# preorder(r)
postorder(r)


class Person(object):
    def __init__(self, name):
        self.name = name


p = Person('abc')
a = Person('abc')

# print(p)
# print(a)
