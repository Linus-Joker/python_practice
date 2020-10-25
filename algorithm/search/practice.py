# 練習 (while or for in) & stack return

# stack = []


# def test():
#     fruits = ['apple', 'banana', 'cherry']
#     # for x in fruits:
#     #     stack.append(x)
#     # return stack

#     while len(fruits) > 0:
#         fruit = fruits.pop()
#         stack.append(fruit)
#     return stack


# rel = test()
# print(rel)


# 練習函式運算

import math

graph = {
    "A": {"B": 1, "C": 2},
    "B": {"A": 1, "D": 1},
    "C": {"A": 2, "D": 2},
    "D": {"B": 1, "C": 2, "E": 2},
    "E": {"D": 2}
}


def init_distance(graph, s):
    distance = {s: 0}
    for vertex in graph:
        # if vertex != s:
        #     distance[vertex] = math.inf
        return vertex


distance = init_distance(graph, "A")

print(distance)
