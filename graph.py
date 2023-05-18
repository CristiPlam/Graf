import json
from pprint import pprint
import pickle

class Graph:
    def __init__(self, graph = None):
        if graph:
            self.edges = graph.edges
            self.vertices = graph.vertices
            self.vert_dict = graph.vert_dict
        else:
            self.edges = []
            self.vertices = []
            self.vert_dict = {}

    def get_vertices(self):
        return self.vertices

    def add_edge(self, vert_1, vert_2):
        for edge in self.edges:
            if edge[0] == vert_1 and edge[1] == vert_2:
                raise IndexError("Edge already exists!")

        self.edges.append((vert_1, vert_2))

    def add_vertex(self, vert):
        for v in self.vertices:
            if vert == v:
                raise IndexError("Vertex already exists!")

        self.vertices.append(vert)

    def get_num_vertices(self):
        return len(self.vertices)

    def read_file(self, file):
        temp = []

        with open(file) as f:
            lines = f.readlines()
        for line in lines:
            temp.append(line.split(" "))

        for line in temp:
            self.edges.append((int(line[0]), int(line[1])))


    def create_vertices(self):
        for edge in self.edges:
            if not self.find_node(edge[0]):
                self.vertices.append(edge[0])
            if not self.find_node(edge[1]):
                self.vertices.append(edge[1])

        self.vertices.sort()

    def find_node(self, node):
        if node in self.vertices:
            return True
        else:
            return False

    def delete_vertex(self, vert):
        self.vertices.remove(vert)

    def delete_edge(self, edge):
        self.edges.remove(edge)

    def get_num_edges(self):
        return len(self.edges)

    def get_num_edges_undirected(self):
        return int(len(self.edges) / 2)


    def get_vert_dict(self):
        for v in self.vertices:
            temp = []
            for edge in self.edges:
                if v in edge:
                    if v == edge[0]:
                        temp.append(edge[1])
                    else:
                        temp.append(edge[0])
            self.vert_dict[v] = temp
            temp = []

        return self.vert_dict

    def is_adjacent(self, vert1, vert2):
        adjacent = False

        for edge in self.edges:
            if (edge[0] == vert1 and edge[1] == vert2) or (edge[0] == vert2 and edge[1] == vert1):
                adjacent = True

        if adjacent == True:
            print("Vertices " + str(vert1) + " and " + str(vert2) + " are adjacent")
        else:
            print("Vertices " + str(vert1) + " and " + str(vert2) + " are NOT adjacent")


    def get_outward_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge[0] == node:
                neighbors.append(edge[1])

        return neighbors

    def get_inward_neighbors(self, node):
        neighbors = []
        for edge in self.edges:
            if edge[1] == node:
                neighbors.append(edge[0])

        return neighbors

    def get_neighbors(self, node):
        return self.get_inward_neighbors(node) + self.get_outward_neighbors(node)


    def contract_edge(self, edge):
        neighbors_out_deleted = self.get_outward_neighbors(edge[0])
        neighbors_in_deleted = self.get_inward_neighbors(edge[0])

        self.get_inward_neighbors(edge[1]) + neighbors_in_deleted
        self.get_outward_neighbors(edge[1]) + neighbors_out_deleted

        for e in self.edges:
            if e[0] == edge[0] or e[1] == edge[0]:
                self.delete_edge(e)

        self.delete_vertex(edge[0])






# graph = Graph()
# file = 'D:/FACULTATE/MASTER/ANUL 2/SEMESTRUL 2/DUCOFFE/Graf/test graf.txt'
# graph.read_file(file)
#
# # print(graph.edges)
# graph.create_vertices()
# print(graph.get_vertices())
# graph.delete_edge((1,3))
# print(graph.edges)
# pickled_graph = pickle.dumps(graph)
# print(pickle.loads(pickled_graph))
# print(pickled_graph)
# print(graph.edges)
# graph.BFS(1)
# print("\n")
# graph.DFS(1)
# print(graph.vertices)
# print(graph.get_num_vertices())
# print(graph.get_num_vertices())

# print(graph.get_num_vertices())
# print(graph.get_num_edges())

# graph.add_vertex(4)
#
# graph.add_edge(2, 4)

# print(graph.vertices)
#
# print(graph.edges)
#
# pprint(graph.get_vert_dict())
#
# graph.is_adjacent(2,3)

# print(graph.get_num_edges_undirected())

# neighbors = graph.get_inward_neighbors(105)
# neighbors2 = graph.get_outward_neighbors(105)

# all_neigh = graph.get_neighbors(105)
# print(all_neigh)

# graph.contract_edge((6, 319))
#
# print(graph.get_neighbors(319))
# print(graph.vertices)
