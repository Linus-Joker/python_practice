class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        print('getter')
        return self.hidden_name

    def set_name(self, input_name):
        print('setter')
        self.hidden_name = input_name

    name = property(get_name, set_name)


fowl = Duck('milk')
print(fowl.name)
print(fowl.get_name())
fowl.name = 'daffy'
print(fowl.name)
