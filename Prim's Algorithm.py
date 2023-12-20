import networkx as nx
import matplotlib.pyplot as plt
import heapq

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

def prim(graph):
    mst_edges = []
    visited = set()
    start_node = list(graph.graph.nodes)[0]  # Start from any node
    # Priority queue to store edges with weights
    pq = [(0, start_node, None)]

    while pq:
        weight, current_node, parent_node = heapq.heappop(pq)

        if current_node not in visited:
            visited.add(current_node)
            if parent_node is not None:
                mst_edges.append((parent_node, current_node, weight))

            for neighbor, edge_data in graph.graph[current_node].items():
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_data['weight'], neighbor, current_node))

    return mst_edges

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

minimum_spanning_tree_edges = prim(graph)
print("Minimum Spanning Tree Edges:", minimum_spanning_tree_edges)

graph.visualize_graph(minimum_spanning_tree_edges)

# Test Case 1
graph1 = Graph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_edge("A", "B", 3)
graph1.add_edge("B", "C", 1)
graph1.add_edge("A", "C", 2)

graph1.visualize_graph()
minimum_spanning_tree_edges1 = prim(graph1)
print("Minimum Spanning Tree Edges (Test Case 1):", minimum_spanning_tree_edges1)
graph1.visualize_graph(minimum_spanning_tree_edges1)

# Test Case 2
graph2 = Graph()
graph2.add_node("A")
graph2.add_node("B")
graph2.add_node("C")
graph2.add_node("D")
graph2.add_edge("A", "B", 1)
graph2.add_edge("B", "C", 2)
graph2.add_edge("C", "D", 1)
graph2.add_edge("A", "C", 4)
graph2.add_edge("B", "D", 7)

graph2.visualize_graph()
minimum_spanning_tree_edges2 = prim(graph2)
print("Minimum Spanning Tree Edges (Test Case 2):", minimum_spanning_tree_edges2)
graph2.visualize_graph(minimum_spanning_tree_edges2)

