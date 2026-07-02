# Task 5.2: BFS function to check if path exists between two nodes
def has_path_bfs(graph, start, goal):
    """Check if a path exists between start and goal using BFS"""
    visited = []
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        if node == goal:
            return True  # Path found!
        if node not in visited:
            visited.append(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    return False  # No path found

# Test the function
print("\n" + "="*50)
print("TASK 5.2: BFS PATH EXISTENCE CHECK")
print("="*50)

# Test cases
test_cases = [
    ('A', 'G'),    # Path exists: A -> C -> G
    ('A', 'H'),    # Path exists: A -> D -> H
    ('A', 'Z'),    # Path does NOT exist (Z not in graph)
    ('E', 'G'),    # Path exists: E -> F -> G
    ('H', 'A'),    # Path does NOT exist (one-way)
]

for start, goal in test_cases:
    result = has_path_bfs(graph, start, goal)
    print(f"Path from {start} to {goal}: {' EXISTS' if result else ' DOES NOT EXIST'}")