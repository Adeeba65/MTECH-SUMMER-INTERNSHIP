# Task 9.1: A* with detailed f(n), g(n), h(n) values at each step
import heapq

def a_star_with_details(graph, start, goal, heuristic):
    """A* search with detailed f(n), g(n), h(n) values at each step"""
    
    # Priority queue: (f(n), g(n), node, path)
    open_list = []
    g_score = {start: 0}
    f_score = {start: heuristic.get(start, 0)}
    heapq.heappush(open_list, (f_score[start], 0, start, [start]))
    
    visited = []
    step = 0
    
    print("="*70)
    print("TASK 9.1: A* SEARCH WITH f(n), g(n), h(n) VALUES")
    print("="*70)
    print(f"Start: {start}, Goal: {goal}")
    print("-" * 70)
    
    print(f"\n Initial State:")
    print(f"  h({start}) = {heuristic.get(start, 0)}")
    print(f"  g({start}) = 0")
    print(f"  f({start}) = {f_score[start]}")
    print("-" * 50)
    
    while open_list:
        step += 1
        # Pop node with minimum f(n)
        f, g, current, path = heapq.heappop(open_list)
        
        print(f"\n Step {step}:")
        print(f"  Popped: '{current}'")
        print(f"   f({current}) = {f}")
        print(f"   g({current}) = {g}")
        print(f"   h({current}) = {heuristic.get(current, 0)}")
        print(f"   Path so far: {' -> '.join(path)}")
        
        # Check if goal reached
        if current == goal:
            print(f"\n Goal '{goal}' reached!")
            print(f" Final Path: {' -> '.join(path)}")
            print(f" Total Cost (g): {g}")
            print(f" Nodes Explored: {len(visited)}")
            print(f" All Visited Nodes: {visited}")
            return path, g, visited
        
        # Mark as visited
        if current not in visited:
            visited.append(current)
        
        # Explore neighbors
        print(f"  🔗 Exploring neighbors of '{current}':")
        
        for neighbor, edge_cost in graph.get(current, {}).items():
            if neighbor in visited:
                print(f"     Skipping '{neighbor}' (already visited)")
                continue
            
            g_new = g + edge_cost
            h_new = heuristic.get(neighbor, 0)
            f_new = g_new + h_new
            
            # Check if this path is better
            if neighbor not in g_score or g_new < g_score[neighbor]:
                g_score[neighbor] = g_new
                f_score[neighbor] = f_new
                new_path = path + [neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, new_path))
                
                print(f"    ➕ Adding '{neighbor}'")
                print(f"       g({neighbor}) = {g_new}")
                print(f"       h({neighbor}) = {h_new}")
                print(f"       f({neighbor}) = {f_new}")
                print(f"       Path: {' -> '.join(new_path)}")
            else:
                print(f"     Skipping '{neighbor}' (better path exists)")
        
        # Show current priority queue
        if open_list:
            pq_display = [(f, n, g) for f, g, n, _ in open_list]
            print(f"\n   Priority Queue after step {step}: {pq_display}")
        else:
            print(f"\n   Priority Queue after step {step}: EMPTY")
        
        print("-" * 50)
    
    print(f"\n Goal '{goal}' not reachable!")
    return None, float('inf'), visited


# ============================================================
# GRAPH FOR A* (From Lab Manual)
# ============================================================
graph_astar = {
    'S': {'A': 2, 'B': 5},
    'A': {'C': 4, 'D': 7},
    'B': {'D': 3, 'E': 6},
    'C': {'F': 5},
    'D': {'F': 2, 'G': 3},
    'E': {'G': 1},
    'F': {'H': 3},
    'G': {'H': 2},
    'H': {}
}

heuristic_astar = {
    'S': 10, 'A': 8, 'B': 7, 'C': 6, 'D': 4,
    'E': 3, 'F': 2, 'G': 1, 'H': 0
}

print("\n Graph (Weighted):")
print("-" * 50)
for node, edges in graph_astar.items():
    if edges:
        print(f"  {node} -> {edges}")
    else:
        print(f"  {node} -> []")

print(f"\n Heuristic Values:")
print("-" * 50)
for node, h in heuristic_astar.items():
    print(f"  h({node}) = {h}")

# ============================================================
# RUN A* FROM S TO H
# ============================================================
print("\n" + "="*70)
path, cost, visited = a_star_with_details(graph_astar, 'S', 'H', heuristic_astar)