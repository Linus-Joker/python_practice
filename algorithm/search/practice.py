# 練習 (while or for in) & stack return

stack = []


def test():
    fruits = ['apple', 'banana', 'cherry']
    # for x in fruits:
    #     stack.append(x)
    # return stack

    while len(fruits) > 0:
        fruit = fruits.pop()
        stack.append(fruit)
    return stack


rel = test()
print(rel)
