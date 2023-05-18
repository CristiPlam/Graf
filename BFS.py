import pickle

from graph import Graph
from multiprocessing import Process, Lock, Pool
from multiprocessing.managers import BaseManager
def bfs(graph, start):
    visited = [False] * (len(graph.edges) + 1)

    queue = []

    queue.append(start)
    visited[start] = True

    while queue:
        start = queue.pop(0)
        print(str(start), end=' ')

        for i in graph.get_vert_dict()[start]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

"#################################################################################"
"##################Parallel BFS###################################################"
class CustomManager(BaseManager):
    pass

def worker(shared_graph:Graph, node_1, node_2):
    shared_graph.delete_edge((node_1, node_2))


def pbfs(graph:Graph, node):
    visited = [False] * (len(graph.edges) + 1)

    queue = []

    queue.append(node)
    visited[node] = True

    CustomManager.register("Graph", Graph)
    with CustomManager() as m_d:
        shared_graph = m_d.Graph(graph)

        while queue:
            node = queue.pop(0)
            print(str(node))

            for i in shared_graph.get_outward_neighbors(node):
                process = list()
                in_neigh = shared_graph.get_inward_neighbors(node)
                for vert in in_neigh:
                    process.append(Process(target=worker, args=(shared_graph, vert, node)))

                for p in process:
                    p.start()

                for p in process:
                    p.join()

                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

        print(shared_graph.get_vertices())


"#################################################################################"

def pooled_pbfs(graph:Graph, node):
    visited = [False] * (len(graph.edges) + 1)

    queue = []

    queue.append(node)
    visited[node] = True

    with Pool(2) as p:  # create 2 processes
        CustomManager.register("Graph", Graph)
        with CustomManager() as m_d:
            shared_graph = m_d.Graph(graph)  # create copy of graph in order to have all processes globally and make sure to carry over the changes to main

            while queue:
                node = queue.pop(0)
                print(str(node))

                for i in shared_graph.get_outward_neighbors(node):

                    in_neigh = shared_graph.get_inward_neighbors(node)

                    p.starmap(worker, [(shared_graph, vert, node) for vert in in_neigh])

                    if visited[i] == False:
                        queue.append(i)
                        visited[i] = True

            print(shared_graph.get_vertices())

"#################################################################################"

if __name__ == '__main__':
    file = 'D:/FACULTATE/MASTER/ANUL 2/SEMESTRUL 2/DUCOFFE/Graf/test graf.txt'
    file2 = 'D:/FACULTATE/MASTER/ANUL 2/SEMESTRUL 2/DUCOFFE/Graf/facebook_combined.txt'


    graph = Graph()

    graph.read_file(file2)


    graph.create_vertices()

    pooled_pbfs(graph, 0)



