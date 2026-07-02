# Task 8.1: Uniform Cost Search (UCS) with priority queue updates
import heapq

def ucs_with_details(graph, start, goal):
    """UCS with detailed priority queue updates at each step"""
    # Priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    visited = []
    step = 0
    
    print("="*60)
    print("TASK 8.1: UCS WITH PRIORITY QUEUE UPDATES")
    print("="*60)
    print(f"Start: {start}, Goal: {goal}")
    print("-" * 60)
    
    print(f"\n Initial Priority Queue: {[(cost, node) for cost, node, _ in pq]}")
    print("-" * 40)
    
    while pq:
        step += 1
        # Pop node with minimum cost
        cost, node, path = heapq.heappop(pq)
        
        print(f"\n Step {step}:")
        print(f"   Popped: '{node}' (Cost: {cost})")
        print(f"   Path so far: {' -> '.join(path)}")
        
        # Check if goal reached
        if node == goal:
            print(f"\n Goal '{goal}' reached!")
            print(f" Final Path: {' -> '.join(path)}")
            print(f" Total Cost: {cost}")
            print(f" Nodes Explored: {len(visited)}")
            return cost, path, visited
        
        # Mark as visited
        if node not in visited:
            visited.append(node)
        
        # Explore neighbors
        print(f"  🔗 Exploring neighbors of '{node}':")
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                new_cost = cost + edge_cost
                new_path = path + [neighbor]
                heapq.heappush(pq, (new_cost, neighbor, new_path))
                print(f"     Adding '{neighbor}' (Cost: {new_cost})")
            else:
                print(f"     Skipping '{neighbor}' (already visited)")
        
        # Show current priority queue
        if pq:
            pq_display = [(c, n) for c, n, _ in pq]
            print(f"\n   Priority Queue after step {step}: {pq_display}")
        else:
            print(f"\n   Priority Queue after step {step}: EMPTY")
        
        print("-" * 40)
    
    print(f"\n Goal '{goal}' not reachable!")
    return float('inf'), [], visited

# Weighted graph with nodes A through J (from lab manual)
graph_ucs = {
    'A': [('B', 4), ('C', 2)],
    'B': [('D', 5), ('E', 10)],
    'C': [('F', 3), ('G', 8)],
    'D': [('H', 6), ('I', 7)],
    'E': [('J', 1)],
    'F': [('J', 4)],
    'G': [('H', 2)],
    'H': [('J', 3)],
    'I': [('J', 2)],
    'J': []
}

print("\n Graph (Weighted):")
print("-" * 40)
for node, edges in graph_ucs.items():
    if edges:
        print(f"  {node} -> {edges}")
    else:
        print(f"  {node} -> []")

# Run UCS from A to J
print("\n" + "="*60)
cost, path, visited = ucs_with_details(graph_ucs, 'A', 'J')

# Additional test cases
print("\n" + "="*60)
print("ADDITIONAL TEST CASES")
print("="*60)

test_cases = [('A', 'H'), ('A', 'E'), ('A', 'I')]

for start, goal in test_cases:
    print(f"\n Searching from {start} to {goal}:")
    cost, path, visited = ucs_with_details_simple(graph_ucs, start, goal)
    if path:
        print(f"   Path: {' -> '.join(path)}")
        print(f"   Cost: {cost}")
    else:
        print(f"   No path found!")

def ucs_with_details_simple(graph, start, goal):
    """Simplified UCS for additional test cases"""
    pq = [(0, start, [start])]
    visited = []
    
    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.append(node)
        
        if node == goal:
            return cost, path, visited
        
        for neighbor, edge_cost in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (cost + edge_cost, neighbor, path + [neighbor]))
    
    return float('inf'), [], visited