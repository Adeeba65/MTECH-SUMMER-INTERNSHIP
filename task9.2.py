# Task 9.2: Delivery Route Graph for Lahore with A* Search
import heapq

def a_star_city(graph, start, goal, heuristic):
    """A* search for city delivery route"""
    
    open_list = []
    g_score = {start: 0}
    f_score = {start: heuristic.get(start, 0)}
    heapq.heappush(open_list, (f_score[start], 0, start, [start]))
    
    visited = []
    step = 0
    
    print("="*70)
    print("TASK 9.2: DELIVERY ROUTE PLANNER - LAHORE CITY")
    print("="*70)
    print(f" Starting Point: {start}")
    print(f" Destination: {goal}")
    print("-" * 70)
    
    print("\n Initial State:")
    print(f"  h({start}) = {heuristic.get(start, 0)}")
    print(f"  g({start}) = 0")
    print(f"  f({start}) = {f_score[start]}")
    print("-" * 50)
    
    while open_list:
        step += 1
        f, g, current, path = heapq.heappop(open_list)
        
        print(f"\n Step {step}:")
        print(f"   Current Location: '{current}'")
        print(f"   f({current}) = {f} (g={g}, h={heuristic.get(current, 0)})")
        print(f"   Route so far: {' -> '.join(path)}")
        
        if current == goal:
            print(f"\n DELIVERY COMPLETE!")
            print(f" Final Route: {' -> '.join(path)}")
            print(f" Total Distance: {g} km")
            print(f" Nodes Explored: {len(visited)}")
            print(f" All Locations Visited: {visited}")
            return path, g, visited
        
        if current not in visited:
            visited.append(current)
        
        print(f"  🔗 Exploring routes from '{current}':")
        
        for neighbor, distance in graph.get(current, {}).items():
            if neighbor in visited:
                print(f"    ⚠️ Skipping '{neighbor}' (already visited)")
                continue
            
            g_new = g + distance
            h_new = heuristic.get(neighbor, 0)
            f_new = g_new + h_new
            
            if neighbor not in g_score or g_new < g_score[neighbor]:
                g_score[neighbor] = g_new
                f_score[neighbor] = f_new
                new_path = path + [neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor, new_path))
                
                print(f"    ➕ Adding '{neighbor}' to route")
                print(f"       Distance so far: {g_new} km")
                print(f"       Estimated remaining: {h_new} km")
                print(f"       Total estimated: {f_new} km")
        
        if open_list:
            pq_display = [(f, n, g) for f, g, n, _ in open_list]
            print(f"\n   Priority Queue: {pq_display}")
        
        print("-" * 50)
    
    print(f"\n No route found from {start} to {goal}!")
    return None, float('inf'), visited


# ============================================================
# LAHORE CITY DELIVERY ROUTE GRAPH (10 Nodes)
# ============================================================
lahore_graph = {
    'Anarkali': {'Mall_Road': 3, 'Gulberg': 5, 'Model_Town': 8},
    'Mall_Road': {'Anarkali': 3, 'Gulberg': 4, 'Johar_Town': 7},
    'Gulberg': {'Anarkali': 5, 'Mall_Road': 4, 'Model_Town': 3, 'Defence': 6},
    'Model_Town': {'Anarkali': 8, 'Gulberg': 3, 'Defence': 5, 'DHA': 9},
    'Defence': {'Gulberg': 6, 'Model_Town': 5, 'DHA': 4, 'Johar_Town': 8},
    'Johar_Town': {'Mall_Road': 7, 'Defence': 8, 'DHA': 3, 'Airport': 5},
    'DHA': {'Model_Town': 9, 'Defence': 4, 'Johar_Town': 3, 'Airport': 7},
    'Airport': {'Johar_Town': 5, 'DHA': 7},
    'Garhi_Shahu': {'Anarkali': 4, 'Mall_Road': 6, 'Gulberg': 7},
    'Ichhra': {'Anarkali': 5, 'Mall_Road': 8, 'Gulberg': 6}
}

# Heuristic: Estimated distance to Airport (in km)
lahore_heuristic = {
    'Anarkali': 12,
    'Mall_Road': 10,
    'Gulberg': 8,
    'Model_Town': 7,
    'Defence': 5,
    'Johar_Town': 4,
    'DHA': 3,
    'Airport': 0,
    'Garhi_Shahu': 13,
    'Ichhra': 11
}

print("\n" + "="*70)
print(" LAHORE CITY DELIVERY ROUTE MAP")
print("="*70)

print("\n Graph (Distances in km):")
print("-" * 50)
for location, routes in lahore_graph.items():
    if routes:
        print(f"  {location} -> {routes}")
    else:
        print(f"  {location} -> []")

print(f"\n Heuristic Values (Estimated Distance to Airport):")
print("-" * 50)
for location, h in lahore_heuristic.items():
    print(f"  h({location}) = {h} km")

print("\n" + "="*70)
print("📍 ROUTE SEARCH: Anarkali to Airport")
print("="*70)

# Run A* from Anarkali to Airport
path, cost, visited = a_star_city(lahore_graph, 'Anarkali', 'Airport', lahore_heuristic)

# ============================================================
# COMPARE DIFFERENT ROUTES
# ============================================================
print("\n" + "="*70)
print(" COMPARING DIFFERENT ROUTES TO AIRPORT")
print("="*70)

def find_route_details(graph, start, goal, heuristic):
    """Simplified A* to find route details"""
    open_list = [(heuristic.get(start, 0), 0, start, [start])]
    visited = []
    g_score = {start: 0}
    
    while open_list:
        f, g, current, path = heapq.heappop(open_list)
        if current in visited:
            continue
        visited.append(current)
        
        if current == goal:
            return path, g, len(visited)
        
        for neighbor, dist in graph.get(current, {}).items():
            if neighbor not in visited:
                g_new = g + dist
                if neighbor not in g_score or g_new < g_score[neighbor]:
                    g_score[neighbor] = g_new
                    f_new = g_new + heuristic.get(neighbor, 0)
                    heapq.heappush(open_list, (f_new, g_new, neighbor, path + [neighbor]))
    
    return None, float('inf'), len(visited)

# Find routes from different starting points
start_locations = ['Anarkali', 'Mall_Road', 'Gulberg', 'Model_Town', 'Defence', 'DHA']

print("\n| Start Location | Route to Airport | Distance (km) | Nodes Explored |")
print("|----------------|------------------|---------------|----------------|")

for start in start_locations:
    path, cost, explored = find_route_details(lahore_graph, start, 'Airport', lahore_heuristic)
    if path:
        route = ' -> '.join(path)
        if len(route) > 16:
            route = route[:14] + '...'
        print(f"| {start:14} | {route:16} | {cost:13} | {explored:14} |")
    else:
        print(f"| {start:14} | No Route Found | N/A           | N/A            |")

# ============================================================
# VISUAL MAP OF LAHORE
# ============================================================
print("\n" + "="*70)
print(" LAHORE CITY MAP VISUALIZATION")
print("="*70)

print("""
                    Garhi_Shahu (h=13)
                       |
                      4|
                       |
                    Anarkali (h=12)
                    /   |   \\
                  3/   5|   8\\
                 /      |      \\
            Mall_Road  Gulberg  Model_Town
            (h=10)     (h=8)    (h=7)
               |       / | \       |
              7|     4/  |  \6     |5
               |     /   |   \     |
            Johar_Town  Ichhra  Defence
            (h=4)      (h=11)  (h=5)
               |         |       |
              5|        6|      4|
               |         |       |
            Airport ---- DHA ----|
            (h=0)      (h=3)
               \         /
                \       /
                 3\   /
                    Johar_Town
""")