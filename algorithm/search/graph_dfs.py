# 深度搜尋練習 DFS， 後進先出(stack)

graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "D"],
    "D": ["B", "C", "E"],
    "E": ["D"],
}

# print(graph.keys())
# print(graph["A"])
# print(len(graph))


def DFS(graph, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    # print(queue)
    while (len(stack) > 0):
        vertex = stack.pop()
        node = graph[vertex]
    # print(node)
        for w in node:
            if w not in seen:
                stack.append(w)
                seen.add(w)
        print("路徑順序:", vertex, "start path:", s)
        # print(queue)


DFS(graph, "A")
