# 廣度搜尋練習 BFS，先進先出(Queue)
import heapq
import math

# graph = {
#     "A": ["B", "C"],
#     "B": ["A", "D"],
#     "C": ["A", "D"],
#     "D": ["B", "C", "E"],
#     "E": ["D"],
# }

# print(graph.keys())
# print(graph["A"])
# print(len(graph))


def BFS(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    # print(queue)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        node = graph[vertex]
    # print(node)
        for w in node:
            if w not in seen:
                queue.append(w)
                seen.add(w)
        print(vertex)
        # print(queue)


# BFS(graph, "A")

# 廣度搜尋練習 BFS，先進先出(Queue)，最短路徑搜尋

def BFS_short_search(graph, s):
    queue = []
    queue.append(s)
    seen = set()
    seen.add(s)
    parent = {s: None}
    # print(queue)
    while (len(queue) > 0):
        vertex = queue.pop(0)
        node = graph[vertex]
    # print(node)
        for w in node:
            if w not in seen:
                queue.append(w)
                seen.add(w)
                parent[w] = vertex
        # print(vertex)
    return parent


# parent = BFS_short_search(graph, "A")
# print(parent)
# v = "D"

# while v != None:
#     print(v)
#     v = parent[v]

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
        if vertex != s:
            distance[vertex] = math.inf
    return distance


def dijkstra(graph, s):
    pqueue = []
    heapq.heappush(pqueue, (0, s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)
    # print(pqueue)

    while (len(pqueue) > 0):
        pair = heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(s)

        node = graph[vertex].keys()
    # print(node)
        for w in node:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w] = vertex
                    distance[w] = dist + graph[vertex][w]

                parent[w] = vertex
        # print(vertex)
    return parent, distance


parent, distance = dijkstra(graph, "A")
print(parent)
print(distance)
