# Task 7.2: GBFS with different heuristic values
def greedy_bfs(graph, start, goal, heuristic):
    """Greedy Best-First Search with custom heuristic"""
    open_list = [start]
    visited = []
    path = []
    nodes_explored = 0
    
    print(f"\n Starting GBFS from '{start}' to '{goal}'")
    print(f" Heuristic: {heuristic}")
    print("-" * 40)
    
    while open_list:
        # Select node with minimum heuristic value
        current = min(open_list, key=lambda n: heuristic.get(n, float('inf')))
        open_list.remove(current)
        
        if current not in visited:
            visited.append(current)
            path.append(current)
            nodes_explored += 1
            print(f"  Step {nodes_explored}: Exploring '{current}' (h={heuristic.get(current, '∞')})")
        
        if current == goal:
            print(f"\n Goal '{goal}' reached!")
            return path, nodes_explored
        
        # Add neighbors to open list
        for neighbor in graph.get(current, []):
            if neighbor not in visited and neighbor not in open_list:
                open_list.append(neighbor)
                print(f"    └─ Added '{neighbor}' to frontier (h={heuristic.get(neighbor, '∞')})")
    
    print(f"\n Goal '{goal}' not reachable!")
    return path, nodes_explored

# Create graph for GBFS
graph_gbfs = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G'],
    'D': ['H'],
    'E': ['G'],
    'F': ['G'],
    'G': [],
    'H': ['G']
}

print("\n" + "="*50)
print("TASK 7.2: GBFS WITH DIFFERENT HEURISTICS")
print("="*50)

# Heuristic Set 1: Good heuristic (accurate estimates)
heuristic_set1 = {
    'A': 7,   # Distance from A to G
    'B': 5,   # Distance from B to G
    'C': 3,   # Distance from C to G
    'D': 6,   # Distance from D to G
    'E': 2,   # Distance from E to G
    'F': 4,   # Distance from F to G
    'G': 0,   # Goal node (distance 0)
    'H': 3    # Distance from H to G
}

# Heuristic Set 2: Poor heuristic (less accurate)
heuristic_set2 = {
    'A': 10,  # Overestimated
    'B': 9,   # Overestimated
    'C': 8,   # Overestimated
    'D': 7,   # Overestimated
    'E': 6,   # Overestimated
    'F': 5,   # Overestimated
    'G': 0,   # Goal node (distance 0)
    'H': 4    # Overestimated
}

# Heuristic Set 3: Misleading heuristic (bad estimates)
heuristic_set3 = {
    'A': 3,   # Underestimated (misleading)
    'B': 1,   # Very low
    'C': 10,  # Very high
    'D': 2,   # Low
    'E': 9,   # High
    'F': 8,   # High
    'G': 0,   # Goal node
    'H': 6    # Medium
}

# Test all heuristic sets
heuristic_sets = [
    ("Heuristic Set 1 (Good)", heuristic_set1),
    ("Heuristic Set 2 (Poor)", heuristic_set2),
    ("Heuristic Set 3 (Misleading)", heuristic_set3)
]

for name, heuristic in heuristic_sets:
    print("\n" + "="*50)
    print(f" {name}")
    print("="*50)
    print(f"Heuristic values: {heuristic}")
    
    path, nodes_explored = greedy_bfs(graph_gbfs, 'A', 'G', heuristic)
    
    print(f"\n Path found: {' -> '.join(path) if path else 'No path'}")
    print(f" Nodes explored: {nodes_explored}")
    print("-" * 40)

# Comparison Table
print("\n" + "="*50)
print("COMPARISON TABLE")
print("="*50)
print("\n| Heuristic Set | Path Found | Nodes Explored |")
print("|---------------|------------|----------------|")

for name, heuristic in heuristic_sets:
    path, nodes_explored = greedy_bfs(graph_gbfs, 'A', 'G', heuristic)
    path_str = ' -> '.join(path) if path else 'None'
    if len(path_str) > 10:
        path_str = path_str[:8] + '...'
    print(f"| {name[:13]:13} | {path_str:10} | {nodes_explored:14} |")