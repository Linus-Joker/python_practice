class ListNode(object):
    def __init__(self, value=None, next=None):
        self.val = value
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def print_nodes(self):
        if not self.head:
            print(self.head)
        node = self.head
        # print(node)
        while node:
            end = " -> " if node.next else "\n"
            print(node.val, end=end)
            node = node.next

    # 插入到最後1個
    def append(self, value):
        if not self.head:
            # print(value)
            self.head = ListNode(value)
            # print(self.head)
            return
        node = self.head
        # print(node)
        # print(node.next)
        while node.next:
            node = node.next
        node.next = ListNode(value)
        # print(node.next)

    # 移除最後一個
    def remove(self):
        node = self.head
        if not node:
            print("List is empty!!")
        while (node.next.next is not None):
            node = node.next
        node.next = None

    # 插入到第1個
    def push(self, value):

        if not self.head:
            self.head = ListNode(value)
            return
        else:
            newnode = ListNode(value)
            newnode.next = self.head
            self.head = newnode

    # 移除第1個
    def removehead(self):
        node = self.head
        if not node:
            print("List is empty!!")
        self.head = node.next
        node = None

    def insert(self, index, value):
        if index >= self.size():
            self.append(value)
            return
        count = 0
        node = self.head
        previous = None
        while node:
            if count == index:
                if previous:
                    new_node = ListNode(value, previous.next)
                    previous.next = new_node
                else:
                    self.head = ListNode(value, node)
                return
            count += 1
            previous = node
            node = node.next

    # 算數量
    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count


link = LinkedList()

link.append(3)
link.append(4)
link.append(5)
link.append(6)
# link.remove()
link.push(2)
link.append(7)
link.push(1)
# link.removehead()
link.insert(3, 8)
link.print_nodes()
print(link.size())
