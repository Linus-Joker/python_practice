class Employee:
    def __init__(self):
        self.cut_tree = 3

    def work(self):
        print('Working')

    def __sleep(self):
        print('Sleeping')


if __name__ == '__main__':
    andy = Employee()

    andy.work()
    # Working
    andy.__sleep()
    # AttributeError: 'Employee' object has no attribute '__sleep'
