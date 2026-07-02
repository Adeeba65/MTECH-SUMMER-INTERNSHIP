# Task 6.1: DFS to find all possible paths from A to F
def dfs_all_paths(graph, start, goal, path=None, all_paths=None):
    """Find all paths from start to goal using DFS (recursive)"""
    if path is None:
        path = [start]
        all_paths = []
    
    # If we reached the goal, save the path
    if start == goal:
        all_paths.append(path[:])  # Copy the path
        return all_paths
    
    # Explore all neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in path:  # Avoid cycles
            dfs_all_paths(graph, neighbor, goal, path + [neighbor], all_paths)
    
    return all_paths

# Create a graph for DFS
graph_dfs = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': ['F'],
    'F': [],
    'G': ['F'],
    'H': ['F']
}

print("="*50)
print("TASK 6.1: DFS - ALL PATHS FROM A TO F")
print("="*50)
print(f"Graph: {graph_dfs}")
print("\n" + "-"*30)

all_paths = dfs_all_paths(graph_dfs, 'A', 'F')

if all_paths:
    print(f" Found {len(all_paths)} path(s) from A to F:\n")
    for i, path in enumerate(all_paths, 1):
        print(f"Path {i}: {' -> '.join(path)}")
else:
    print(" No path found from A to F")