# Task 5.1: BFS Traversal on a graph with 8+ nodes
def bfs_traversal(graph, start):
    """BFS traversal - returns the order of visited nodes"""
    visited = []           # List to keep track of visited nodes
    queue = [start]        # Queue for BFS (FIFO)
    
    while queue:
        node = queue.pop(0)  # Remove first element from queue
        if node not in visited:
            visited.append(node)  # Mark as visited
            print(f"Visiting: {node}")  # Show traversal step
            
            # Add all unvisited neighbors to the queue
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    return visited

# Create a graph with 8 nodes (City Map)
graph = {
    'A': ['B', 'C', 'D'],     # A connects to B, C, D
    'B': ['E', 'F'],          # B connects to E, F
    'C': ['G'],               # C connects to G
    'D': ['H'],               # D connects to H
    'E': [],                  # E has no connections
    'F': ['G'],               # F connects to G
    'G': [],                  # G has no connections
    'H': []                   # H has no connections
}

print("="*50)
print("TASK 5.1: BFS TRAVERSAL")
print("="*50)
print(f"Graph: {graph}")
print("\nBFS Traversal starting from node 'A':")
print("-" * 30)

traversal_order = bfs_traversal(graph, 'A')
print("-" * 30)
print(f"Traversal Order: {traversal_order}")