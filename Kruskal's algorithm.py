import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

    def visualize_graph(self, tree_edges=None):
        pos = nx.spring_layout(self.graph)
        nx.draw(self.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)

        if tree_edges:
            tree_edges_graph = nx.Graph()
            tree_edges_graph.add_weighted_edges_from(tree_edges)
            nx.draw_networkx_edges(tree_edges_graph, pos, edge_color='red', width=2)

        plt.title("Graph Visualization")
        plt.show()

def kruskal(graph):
    mst_edges = []
    edge_list = [(edge[2]['weight'], edge) for edge in graph.graph.edges(data=True)]
    edge_list.sort()

    union_find = {node: node for node in graph.graph.nodes}

    for weight, edge in edge_list:
        node1, node2 = edge[0], edge[1]
        root1 = find(union_find, node1)
        root2 = find(union_find, node2)

        if root1 != root2:
            mst_edges.append((node1, node2, weight))
            union(union_find, root1, root2)

    return mst_edges

def find(union_find, node):
    if union_find[node] != node:
        union_find[node] = find(union_find, union_find[node])
    return union_find[node]

def union(union_find, root1, root2):
    union_find[root1] = root2

# Sample Graph
graph = Graph()
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_edge("A", "B", 2)
graph.add_edge("B", "C", 1)
graph.add_edge("A", "C", 4)
graph.add_edge("C", "D", 3)
graph.add_edge("B", "D", 7)

graph.visualize_graph()

minimum_spanning_tree_edges = kruskal(graph)
print("Minimum Spanning Tree Edges:", minimum_spanning_tree_edges)

graph.visualize_graph(minimum_spanning_tree_edges)
