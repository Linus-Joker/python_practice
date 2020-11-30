class Student:
    def __init__(self):
        self.name = ''
        self.sorce = 0
        self.next = None


head = Student()
head.next = None
ptr = head

one = Student()
one.name = 'linus'
one.sorce = 99
ptr.next = one  # 這再者裡將one 指派給head.next
# print(head.next)
one.next = None
ptr = ptr.next
# print(head.next)

two = Student()
two.name = 'anna'
two.sorce = 98
ptr.next = two
two.next = None
ptr = ptr.next

ptr = head.next
# print(ptr)
while ptr != None:
    print(ptr)
    print(ptr.name, ptr.sorce)
    ptr = ptr.next

# print(head.next)
