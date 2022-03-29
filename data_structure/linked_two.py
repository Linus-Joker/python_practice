class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("List is empty.")
        else:
            current = self.head
            while current is not None:
                print(current.value, end=' ')
                current = current.next

    # 放資料在List的最前面
    def insert_front(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # 放資料在List的最後面
    def insert_back(self, data):
        newNode = Node(data)

        if self.head is None:
            self.insert_front(data)
        else:
            temporaryList = self.head
            while(temporaryList.next is not None):
                temporaryList = temporaryList.next
            temporaryList.next = newNode

    # 更新開頭資料
    def update_front(self, data):
        if self.head is None:
            print("list is empty.")
        else:
            self.head.value = data

    # 更新尾端資料
    def update_back(self, data):
        if self.head is None:
            print("List is empty.")
        else:
            temporaryList = self.head
            while(temporaryList.next is not None):
                temporaryList = temporaryList.next
            temporaryList.value = data

    # 移除開頭資料
    def remove_front(self):
        temporaryList = self.head
        if temporaryList is None:
            print("List is empty.")
        else:
            self.head = temporaryList.next
            temporaryList = None

    # 移除尾端資料
    def remove_back(self):
        temporaryList = self.head
        if temporaryList is None:
            print("List is empty.")
        else:
            while(temporaryList.next.next is not None):
                temporaryList = temporaryList.next
            temporaryList.next = None

    # 新增資料到中間，用指定的方式
    def insert_middle(self, num, data):
        newNode = Node(data)
        temporaryList = self.head
        if temporaryList is None:
            print("List is empty.")
        else:
            while(temporaryList.value is not num):
                temporaryList = temporaryList.next
            newNode.next = temporaryList.next
            temporaryList.next = newNode

    # 刪除節點
    def DeleteData(self, data):  # 刪除list中的T data資料
        previous = None
        current = self.head

        # 如果current為null或current的資料為我們所要刪除的就停止traversal
        while (current is not None and current.value != data):
            previous = current
            current = current.next

        if current is None:  # current為null代表list為空或是list中不存在我們想要刪除的資料
            print("There is no " + str(data) + " in list")
        elif current == self.head:  # 如果我們想要刪除的資料是第一個節點
            self.head = current.next
            current = None
        else:  # 想要刪除的資料不是第一個節點
            previous.next = current.next

            # 基本上這個是0或None都沒查，除非你知道它記憶體位置並且要把它列印出來
            # 因為上面那行104，把中間斷掉又重新連起來
            current = 0

    # 更新節點
    # 用的是線性搜尋找到相對的值把它替換掉
    def update_data(self, num, data):
        current = self.head
        if current.value != num:
            current = current.next

        current.value = data


list = LinkedList()

# 新增資料，因為List沒資料所以會去新增在最前面
list.insert_back(1)

# 新增資料，在尾端加入資料
list.insert_back(2)
list.insert_back(3)

# 印出資料，Linked搜尋是線性
list.print_list()  # 1 2 3

# 移除尾端資料
print("開始移除尾端資料")
list.remove_back()
list.print_list()  # 1 2

# 移除開頭資料
print("開始移除開頭資料")
list.remove_front()
list.print_list()  # 2

print("開始更新開頭資料")
list.update_front(70)
list.print_list()  # 70

print("再新增資料")
# 新增資料，在尾端加入資料
list.insert_back(2)
list.insert_back(3)
list.print_list()  # 70 2 3

print("更新尾端資料")
# 更新尾端資料
list.update_back(80)
list.print_list()  # 70 2 80

print("開始新增資料到2和80中間")
list.insert_middle(2, 10)
list.print_list()  # 70 2 10 80

print("開始新增資料到10和80中間")
list.insert_middle(10, 16)
list.print_list()  # 70 2 10 16 80

# print("開始刪除頭部節點")
# list.DeleteData(70)
# list.print_list()

# print("開始刪除節點")
# list.DeleteData(2)
# list.print_list()

print("更新資料")
list.update_data(70, 71)
list.print_list()  # 71 2 10 16 80

print("更新資料")
list.update_data(2, 3)
list.print_list()  # 71 3 10 16 80
