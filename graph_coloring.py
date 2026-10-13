"""
Graph Coloring using the Greedy Algorithm
Run with: python graph_coloring.py
"""

def greedy_coloring(graph):
    """
    graph: dictionary where each vertex maps to its neighboring vertices.
    Returns a dictionary mapping each vertex to a color number.
    """
    colors = {}

    for vertex in graph:
        used_colors = {colors[neighbor] for neighbor in graph[vertex]
                       if neighbor in colors}

        color = 0
        while color in used_colors:
            color += 1

        colors[vertex] = color

    return colors


if __name__ == "__main__":
    # Example graph (undirected)
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C", "E"],
        "E": ["D"],
    }

    result = greedy_coloring(graph)

    print("Graph Coloring (Greedy Algorithm)")
    for vertex, color in result.items():
        print(f"Vertex {vertex}: Color {color + 1}")

    print(f"\nNumber of colors used: {len(set(result.values()))}")
