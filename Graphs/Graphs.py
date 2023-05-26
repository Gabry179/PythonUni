def create():
    return dict()

def add_node(graph, node):
    if not node in graph:
        graph[node] = []
    return graph

def add_nodes(graph, nodes):
    for node in nodes:
        add_node(graph, node)
    return graph

def get_nodes(graph):
    return list(graph.keys())

def nodes_count(graph):
    return len(graph)

def remove_vertex(graph, v):
    if v in graph:
        for node in graph[v]:
            graph[node].remove(v)
        del graph[v]
    return graph

def add_edge(graph, u, v):
    if u in graph and v in graph:
        if v not in graph[u]:
            graph[u].append(v)
        if u not in graph[v]:
            graph[v].append(u)
    return graph

def add_edges(graph, edges):
    for edge in edges:
        add_edge(graph, *edge)
    return graph

def get_edge(graph, edge):
    u, v = edge
    if u in graph[v] and v in graph[u]:
        return True
    else:
        return False

def get_edges(graph):
    edges = []
    for k, v in graph.items():
        for u in v:
            if(k, u) not in edges and (u, k) not in edges:
                edges.append((k, u))
    return edges

def edges_count(graph):
    return len(get_edges(graph))

def incident_edges(graph, u):
    edges = []
    if u in graph:
        for node in graph[u]:
            edges.append((u, node))
    return edges

def remove_edge(graph, edge):
    u, v = edge
    if u not in graph or v not in graph:
        print("One of the nodes doesn't exist")
    else:
        if u in graph[v]:
            graph[v].remove(u)
        if v in graph[u]:
            graph[u].remove(v)
    return graph

def degree(graph):
    deg = dict()
    for node in graph:
        deg[node] = len(graph[node])
    return deg

def is_complete(graph):
    n = len(graph)
    for node in graph:
        if len(graph) < n-1:
            return False
    return True

def dfs_iterative(graph, start):
    explored = []
    stack = []
    stack.append(start)
    while stack:
        u = stack.pop()
        if u not in explored:
            explored.append(u)
            for v in list(graph[u]):
                stack.append(v)
    return explored

def bfs(graph, s):
    exploration = dict()
    for u in get_nodes(graph):
        if u != s:
            exploration[u] = -1
    print("Exploration[]: %s" % (exploration))

    exploration[s] = 0
    stack = list()
    stack.append(s)
    print("Stacking %s, Q[]: %s" % (s, stack))
    print("Exploration[]: %s" % (exploration))

    while stack:
        u = stack.pop()
        print("Exploring vertex adjacent to %s (u)" % (u))
        for v in graph[u]:
            print("Exploration[v] = %s is -1 (white)? Exploration[]: %s" % (exploration[v], exploration))
            if exploration[v] == -1:
                exploration[v] = 0
                stack.append(v)
                print("Stacking %s, Q[]: %s" % (v, stack))
                print("Exploration[]: %s" % (exploration))
        exploration[u] = 1
        print("Exploration[u] = %s is 1 (black), Exploration[]: %s" % (exploration[u], exploration))
    return exploration
   
def main():
    graph = create()
    #add_node(graph, "node1")
    add_nodes(graph, ['SFO','ORD','BOS','JFK','DFW','LAX','MIA'])
    add_edges(graph, [ 
        ['BOS','SFO'],
        ['BOS','JFK'],
        ['BOS','MIA'],
        ['JFK','SFO'],
        ['JFK','BOS'],
        ['JFK','DFW'],
        ['JFK','MIA'],
        ['ORD','DFW'],
        ['ORD','MIA'],
        ['DFW','ORD'],
        ['DFW','SFO'],
        ['DFW','LAX'],
        ['MIA','DFW'],
        ['MIA','LAX'],
    ])
    print("Nodes: " + str(get_nodes(graph)))
    print("Number of nodes: " + str(nodes_count(graph)))
    print("Edge between SFO and JFK: " + str(get_edge(graph, ('SFO', 'JFK'))))
    print("Edges: " + str(get_edges(graph)))
    print("Total edges count: " + str(edges_count(graph)))
    print("Incident edges in SFO: " + str(incident_edges(graph, ('SFO'))))
    print("Degrees: " + str(degree(graph)))
    print("Is the graph complete?: " + str(is_complete(graph)))
    print("DFS: " + str(dfs_iterative(graph, 'SFO')))
    print("BFS: " + str(bfs(graph, 'LAX')))

if __name__ == "__main__":
    main()