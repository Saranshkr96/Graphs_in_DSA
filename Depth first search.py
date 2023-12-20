import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start_node):
    visited = set()

    def dfs_recursive(node):
        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)
            for neighbor in graph[node]:
                dfs_recursive(neighbor)

    dfs_recursive(start_node)
    
def visualize_graph(graph):
    nx_graph = nx.Graph(graph)
    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8,  connectionstyle="arc3,rad=0.1")
    plt.title("Graph Visualization")
    plt.show()

# Sample Graph 1
graph_1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

visualize_graph(graph_1)
print("DFS starting from node 'A' for Graph 1:")
dfs(graph_1, 'A')

# Sample Graph 2
graph_2 = {
    '1': ['2', '3'],
    '2': ['1', '4', '5'],
    '3': ['1', '6', '7'],
    '4': ['2'],
    '5': ['2'],
    '6': ['3'],
    '7': ['3']
}

visualize_graph(graph_2)
print("\nDFS starting from node '1' for Graph 2:")
dfs(graph_2, '1')

# Sample Graph 3
graph_3 = {
    'X': ['Y', 'Z'],
    'Y': ['X', 'W', 'V'],
    'Z': ['X', 'U'],
    'W': ['Y'],
    'V': ['Y'],
    'U': ['Z']
}

visualize_graph(graph_3)
print("\nDFS starting from node 'X' for Graph 3:")
dfs(graph_3, 'X')
