from graph import Graph


def dfs_util(graph, v, visited):
    visited.add(v)
    print(v, end=' ')

    for neighbour in graph.get_vert_dict()[v]:
        if neighbour not in visited:
            dfs_util(graph, neighbour, visited)

def dfs(graph, v):
    visited = set()

    dfs_util(graph, v, visited)

"############################################################################"

file = file = 'D:/FACULTATE/MASTER/ANUL 2/SEMESTRUL 2/DUCOFFE/Graf/test graf.txt'

graph = Graph()

graph.read_file(file)

print(graph.edges)

graph.create_vertices()

dfs(graph, 1)