# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 22:29:05 2022

@author: s
"""

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
    return path



graph = Graph()
edges = [
    ('Orumiyeh', 'Kermanshah', 54),
    ('Kermanshah', 'ShahrKord', 52),
    ('Kermanshah', 'Ilam', 17),
    ('Kermanshah', 'Yasooj', 78),
    ('Ilam', 'Yasooj', 87),
    ('Ilam', 'Ahvaz', 45),
    ('Ahvaz', 'Boushehr', 45),
    ('Boushehr', 'Yasooj', 29),
    ('Boushehr', 'Mashhad', 160),
    ('Yasooj', 'ShahrKord', 26),
    ('Yasooj', 'Esfahan', 33),
    ('ShahrKord', 'Esfahan', 10),
    ('Esfahan', 'Gorgan', 82),
    ('Esfahan', 'Mashhad', 110)
]


for edge in edges:
    graph.addEdge(*edge)
    
dijkstra(graph, 'Boushehr', 'Gorgan')
