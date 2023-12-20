import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self):
        self.graph = nx.DiGraph()  # Use DiGraph for directed edges

    def add_node(self, value):
        self.graph.add_node(value)

    def add_edge(self, from_node, to_node, weight):
        self.graph.add_edge(from_node, to_node, weight=weight)

def dynamic_programming_shortest_path(graph, source, destination):
    nodes = list(graph.nodes)
    optimal_costs = {node: float('inf') for node in nodes}
    optimal_costs[source] = 0

    for _ in range(len(nodes)):
        changed = False

        for node in nodes:
            for successor in graph.successors(node):
                cost = graph[node][successor]['weight']
                if optimal_costs[successor] > cost + optimal_costs[node]:
                    optimal_costs[successor] = cost + optimal_costs[node]
                    changed = True

    return optimal_costs[destination]

def visualize_graph(graph):
    pos = nx.spring_layout(graph.graph)  # positions for all nodes
    nx.draw(graph.graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, connectionstyle="arc3,rad=0.1")
    edge_labels = nx.get_edge_attributes(graph.graph, 'weight')
    nx.draw_networkx_edge_labels(graph.graph, pos, edge_labels=edge_labels)
    plt.title("Graph Visualization")
    plt.show()

def print_optimal_costs(optimal_costs):
    for node, cost in optimal_costs.items():
        print(f"Optimal cost from node {node} to destination: {cost}")

# Test Case 1
graph1 = Graph()
graph1.add_node("A")
graph1.add_node("B")
graph1.add_node("C")
graph1.add_node("D")
graph1.add_edge("A", "B", 2)
graph1.add_edge("B", "C", 1)
graph1.add_edge("A", "C", 4)
graph1.add_edge("C", "D", 3)
graph1.add_edge("B", "D", 7)

visualize_graph(graph1)
source_node1 = "A"
destination_node1 = "D"
optimal_cost1 = dynamic_programming_shortest_path(graph1.graph, source_node1, destination_node1)
print(f"Optimal cost from node {source_node1} to {destination_node1}: {optimal_cost1}")

# Print additional paths
print(f"Optimal cost from node B to D: {dynamic_programming_shortest_path(graph1.graph, 'B', 'D')}")
print(f"Optimal cost from node C to D: {dynamic_programming_shortest_path(graph1.graph, 'C', 'D')}")
print(f"Optimal cost from node D to D: {dynamic_programming_shortest_path(graph1.graph, 'D', 'D')}")

print()

# Test Case 2
graph2 = Graph()
graph2.add_node("A")
graph2.add_node("B")
graph2.add_node("C")
graph2.add_node("D")
graph2.add_edge("A", "B", 2)
graph2.add_edge("B", "C", 1)
graph2.add_edge("A", "C", 4)
graph2.add_edge("C", "D", 3)
graph2.add_edge("B", "D", 7)
graph2.add_edge("A", "D", 8)

visualize_graph(graph2)
source_node2 = "A"
destination_node2 = "D"
optimal_cost2 = dynamic_programming_shortest_path(graph2.graph, source_node2, destination_node2)
print(f"Optimal cost from node {source_node2} to {destination_node2}: {optimal_cost2}")

# Print additional paths
print(f"Optimal cost from node B to D: {dynamic_programming_shortest_path(graph2.graph, 'B', 'D')}")
print(f"Optimal cost from node C to D: {dynamic_programming_shortest_path(graph2.graph, 'C', 'D')}")
print(f"Optimal cost from node D to D: {dynamic_programming_shortest_path(graph2.graph, 'D', 'D')}")

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

visualize_graph(graph3)
source_node3 = "A"
destination_node3 = "D"
optimal_cost3 = dynamic_programming_shortest_path(graph3.graph, source_node3, destination_node3)
print(f"Optimal cost from node {source_node3} to {destination_node3}: {optimal_cost3}")

# Print additional paths
print(f"Optimal cost from node B to D: {dynamic_programming_shortest_path(graph3.graph, 'B', 'D')}")
print(f"Optimal cost from node C to D: {dynamic_programming_shortest_path(graph3.graph, 'C', 'D')}")
print(f"Optimal cost from node D to D: {dynamic_programming_shortest_path(graph3.graph, 'D', 'D')}")
