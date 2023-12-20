import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def floyd_warshall(graph):
    nodes = graph.nodes
    distances = {node: {other_node: float('infinity') for other_node in nodes} for node in nodes}

    for node in nodes:
        distances[node][node] = 0

    for edge in graph.edges:
        distances[edge[0]][edge[1]] = graph[edge[0]][edge[1]]['weight']

    for k in nodes:
        for i in nodes:
            for j in nodes:
                if distances[i][k] + distances[k][j] < distances[i][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]

    return distances

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

# Test Case 1
graph1 = Graph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_edge("A", "B", 2)
graph1.add_edge("B", "C", 1)
graph1.add_edge("A", "C", 4)
print("Test Case 1:")
visualize_graph(graph1)
all_shortest_distances_1 = floyd_warshall(graph1.graph)
print("All Shortest Distances:")
for source, distances in all_shortest_distances_1.items():
    print(f"From {source}:", distances)
print()

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
print("Test Case 2:")
visualize_graph(graph2)
all_shortest_distances_2 = floyd_warshall(graph2.graph)
print("All Shortest Distances:")
for source, distances in all_shortest_distances_2.items():
    print(f"From {source}:", distances)
print()

# Test Case 3
graph3 = Graph()
graph3.add_node("A")
graph3.add_node("B")
graph3.add_node("C")
graph3.add_node("D")
graph3.add_edge("A", "B", 3)
graph3.add_edge("B", "C", 1)
graph3.add_edge("C", "D", 5)
graph3.add_edge("A", "C", 2)
graph3.add_edge("B", "D", 2)
print("Test Case 3:")
visualize_graph(graph3)
all_shortest_distances_3 = floyd_warshall(graph3.graph)
print("All Shortest Distances:")
for source, distances in all_shortest_distances_3.items():
    print(f"From {source}:", distances)
