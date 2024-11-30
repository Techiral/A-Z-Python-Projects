import heapq

def dijkstra(graph, start):
    # Initialize distances and predecessors
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    predecessors = {}
    
    # Priority queue to keep track of vertices to visit
    vertices_to_visit = [(0, start)]

    while vertices_to_visit:
        current_distance, current_vertex = heapq.heappop(vertices_to_visit)

        # If the current distance is larger than the stored distance, skip it
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = current_vertex
                heapq.heappush(vertices_to_visit, (distance, neighbor))

    return distances, predecessors

# Example graph as an adjacency dictionary
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
distances, predecessors = dijkstra(graph, start_vertex)

# Print the shortest distances and paths from the start vertex
for vertex, distance in distances.items():
    path = [vertex]
    while vertex != start_vertex:
        vertex = predecessors[vertex]
        path.insert(0, vertex)
    print(f'Shortest path to {vertex}: {path}, Distance: {distance}')
