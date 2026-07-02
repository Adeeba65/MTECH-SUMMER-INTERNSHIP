# Task 6.2: Depth-Limited Search (DLS) with different limits
def dls(graph, start, goal, limit, depth=0, visited=None, path=None):
    """Depth-Limited Search - explores nodes up to a certain depth"""
    if visited is None:
        visited = []
        path = []
    
    # Add current node to path and visited
    path = path + [start]
    visited.append(start)
    
    # Print current exploration step
    print(f"  Depth {depth}: Visiting {start}" + (f" (Goal reached!)" if start == goal else ""))
    
    # Check if we reached the goal
    if start == goal:
        return True, visited, path
    
    # Stop if we reached the depth limit
    if depth >= limit:
        print(f"   Reached depth limit {limit} at {start}")
        return False, visited, path
    
    # Explore neighbors
    for neighbor in graph.get(start, []):
        if neighbor not in visited:  # Avoid cycles
            found, new_visited, new_path = dls(graph, neighbor, goal, limit, depth + 1, visited[:], path[:])
            if found:
                return True, new_visited, new_path
    
    return False, visited, path

print("\n" + "="*50)
print("TASK 6.2: DLS WITH DIFFERENT LIMITS")
print("="*50)

print("\n" + "-"*30)
print("COMPARISON: DLS with limit=2 vs limit=4")
print("-"*30)

# Test DLS with limit = 2
print("\n🔍 DLS with LIMIT = 2:")
print("-" * 20)
found, visited, path = dls(graph_dfs, 'A', 'F', 2)
print(f"\nResult: {' Goal F found!' if found else ' Goal F NOT found'}")
print(f"Visited nodes: {visited}")
print(f"Path to goal (if found): {path if found else 'N/A'}")

# Test DLS with limit = 4
print("\n" + "-"*20)
print("\n DLS with LIMIT = 4:")
print("-" * 20)
found, visited, path = dls(graph_dfs, 'A', 'F', 4)
print(f"\nResult: {' Goal F found!' if found else ' Goal F NOT found'}")
print(f"Visited nodes: {visited}")
print(f"Path to goal (if found): {path if found else 'N/A'}")