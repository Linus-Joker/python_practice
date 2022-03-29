import re
from numpy import sort

# 所有數值都是一個一個的節點
# (當成單一的節點+ 推疊的方式看會比較好理解)
# 節點


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# 丟值進來
# (ps.空頭節點丟進來會發生錯誤，所以要先產生頭部節點)
# 判斷 值比節點的值大or小
# 一樣的值要返回節點(這部份晚點說)
# 將root的下一個遞迴insert()
# 如果下一個節點為空則返回這個空節點
# 並存入root的下一個(以此類推)
# ps.記得!! 第2次以後丟的都是空節點(直到你把值放進去為止)


def insert(root, value):
    if root == None:
        return Node(value)
    else:
        if value == root.value:
            return root
        elif value > root.value:
            root.right = insert(root.right, value)
        else:
            root.left = insert(root.left, value)
    return root


r = Node(45)
data = [40, 50, 30, 60, 70, 32, 44, 55, 28]
for i in data:
    insert(r, i)

# 依linked list 特性，搜尋重頭開始
# BST有3種搜尋方式

# 中序追蹤(左中右)(對稱追蹤)


def print_tree(node):
    if node is not None:
        print_tree(node.left)
        print(node.value)
        print_tree(node.right)


print_tree(r)

# 前序追蹤(中左右)(深度追蹤)


def pre_order(node):
    if node is not None:
        print(node.value)
        pre_order(node.left)
        pre_order(node.right)


# pre_order(r)

# 後序追蹤(左右中)(廣度追蹤)
def post_order(node):
    if node is not None:
        post_order(node.left)
        post_order(node.right)
        print(node.value)


# post_order(r)
