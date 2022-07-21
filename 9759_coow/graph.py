from collections import defaultdict
class Graph():
    def __init__(self):
        self.edges = defaultdict(list)
        self.weights = {}
    def addEdge(self, fromVerex, toVertex, weight):
        self.edges[fromVerex].append(toVertex)
        self.edges[toVertex].append(fromVerex)
        self.weights[(fromVerex, toVertex)] = weight
        self.weights[(toVertex, fromVerex)] = weight     
def dijkstra(myGraph, initial, end):
    shortestPaths = {initial: (None, 0)}
    currentVertex = initial
    visited = set()
    while currentVertex != end:
        visited.add(currentVertex)
        destinations = graph.edges[currentVertex]
        weightToCurrentVertex = shortestPaths[currentVertex][1]
        for nextVertex in destinations:
            weight = graph.weights[(currentVertex, nextVertex)] + weightToCurrentVertex
            if nextVertex not in shortestPaths:
                shortestPaths[nextVertex] = (currentVertex, weight)
            else:
                currentShortestWeight = shortestPaths[nextVertex][1]
                if currentShortestWeight > weight:
                    shortestPaths[nextVertex] = (currentVertex, weight)        
        nextDestinations = {vertex: shortestPaths[vertex] for vertex in shortestPaths if vertex not in visited}
        if not nextDestinations:
            return "Route Not Possible"
        currentVertex = min(nextDestinations, key=lambda k: nextDestinations[k][1])
    path = []
    while currentVertex is not None:
        path.append(currentVertex)
        nextVertex = shortestPaths[currentVertex][0]
        currentVertex = nextVertex
    path = path[: : -1]
    return path, nextDestinations[end][1]
graph = Graph()
edges = []
P = int(input())
for i in range(P):
    m, n, w = input().split()
    edges.append((m,n,int(w)))

for edge in edges:
    graph.addEdge(*edge)

len_cow = {}
for i in edges:
    if i[0] == i[0].upper():
        len_cow[i[0]] = (dijkstra(graph, i[0], 'Z'))[1]
        

[print(key, value) for key, value in len_cow.items() if value == min(len_cow.values())]


































