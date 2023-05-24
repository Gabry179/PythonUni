# Trovare il cammino minimo dal nodo sorgente s al nodo destinazione t. Scrivere i passaggi intermedi (i.e., il contenuto della coda di attraversamento)
from queue import PriorityQueue

graph = {
    's': {'s1':1, 's2':3},
    's1': {'s':1, 's3':8, 's4':4},
    's3': {'s1':8, 's5':1, 't':7},
    't': {'s3':7, 's5':10},
    's5': {'t':10, 's3':1, 's4':1},
    's4': {'s5':1, 's1':4, 's2':3},
    's2': {'s':3, 's4':3}
}
visited = list()
def dijkstra(graph, start_vertex):
    D = {v:float('inf') for v in range(len(graph))}
    D[start_vertex] = 0

    pq = PriorityQueue()
    pq.put((0, start_vertex))

    while not pq.empty():
        (dist, current_vertex) = pq.get()
        visited.append(current_vertex)

        for neighbor in range(len(graph)):
            if graph.edges[current_vertex][neighbor] != -1:
                distance = graph.edges[current_vertex][neighbor]
                if neighbor not in graph.visited:
                    old_cost = D[neighbor]
                    new_cost = D[current_vertex] + distance
                    if new_cost < old_cost:
                        pq.put((new_cost, neighbor))
                        D[neighbor] = new_cost
    return D

print(dijkstra(graph, 's'))