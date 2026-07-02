# Task 7.1: IDS with iteration and depth counting
def dls_ids(graph, node, goal, limit, depth=0, visited=None):
    """DLS for IDS - returns True if goal found"""
    if visited is None:
        visited = []
    visited.append(node)
    
    if node == goal:
        return True, visited
    
    if limit <= 0:
        return False, visited
    
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            found, new_visited = dls_ids(graph, neighbor, goal, limit - 1, depth + 1, visited[:])
            if found:
                return True, new_visited
    
    return False, visited

def ids_with_stats(graph, start, goal, max_depth=10):
    """IDS with statistics tracking"""
    print("="*50)
    print("TASK 7.1: IDS WITH ITERATION COUNTING")
    print("="*50)
    
    total_iterations = 0
    depth_levels_explored = []
    
    print(f"Searching for goal '{goal}' from start '{start}'")
    print("-" * 40)
    
    for depth in range(max_depth):
        total_iterations += 1
        print(f"\n🔍 Iteration {total_iterations}: Searching at depth limit = {depth}")
        
        found, visited = dls_ids(graph, start, goal, depth)
        depth_levels_explored.append({
            'depth': depth,
            'nodes_visited': len(visited),
            'visited_nodes': visited,
            'found': found
        })
        
        print(f"   Nodes visited at depth {depth}: {len(visited)}")
        print(f"  Nodes: {visited}")
        
        if found:
            print(f"\n Goal '{goal}' found at depth {depth}!")
            print(f" Total iterations: {total_iterations}")
            print(f" Depth levels explored: {[d['depth'] for d in depth_levels_explored]}")
            print(f" Path: {' -> '.join(visited)}")
            return True, total_iterations, depth_levels_explored
    
    print(f"\n Goal '{goal}' NOT found within depth limit {max_depth}")
    return False, total_iterations, depth_levels_explored

# Create graph for IDS
graph_ids = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

print("\n" + "="*50)
print("IDS WITH STATISTICS")
print("="*50)
print(f"Graph: {graph_ids}")

# Run IDS
found, iterations, depth_stats = ids_with_stats(graph_ids, 'A', 'G')

# Print detailed summary
print("\n" + "="*50)
print("DETAILED SUMMARY")
print("="*50)
print("\n| Depth | Nodes Visited | Goal Found? |")
print("|-------|---------------|-------------|")
for stat in depth_stats:
    print(f"| {stat['depth']:5} | {stat['nodes_visited']:13} | {' Yes' if stat['found'] else ' No':11} |")