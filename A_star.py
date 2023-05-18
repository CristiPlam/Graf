import heapq


def a_star_search(graph, start_vertex, goal_vertex):
    # Create priority queue and visited set
    priority_queue = [(0, start_vertex)]
    visited = set()

    # Create dictionary to store the total cost from start_vertex to each vertex
    g_scores = {start_vertex: 0}

    # Create dictionary to store the estimated total cost from start_vertex to goal_vertex
    f_scores = {start_vertex: graph.heuristic(start_vertex, goal_vertex)}

    while priority_queue:
        # Get the vertex with the minimum f_score
        current_cost, current_vertex = heapq.heappop(priority_queue)

        # Check if we have reached the goal vertex
        if current_vertex == goal_vertex:
            return reconstruct_path(goal_vertex)

        # Mark current_vertex as visited
        visited.add(current_vertex)

        # Explore neighbors of current_vertex
        for neighbor, weight in graph.get_outward_neighbors(current_vertex):
            if neighbor in visited:
                continue

            # Calculate the cost from start_vertex to neighbor
            new_cost = g_scores[current_vertex] + weight

            if neighbor not in g_scores or new_cost < g_scores[neighbor]:
                # Update g_score and f_score
                g_scores[neighbor] = new_cost
                f_scores[neighbor] = new_cost + graph.heuristic(neighbor, goal_vertex)

                # Add neighbor to the priority queue
                heapq.heappush(priority_queue, (f_scores[neighbor], neighbor))

    # If the goal vertex is not reachable, return None
    return None


def reconstruct_path(goal_vertex):
    path = [goal_vertex]
    current_vertex = goal_vertex

    while current_vertex.parent:
        current_vertex = current_vertex.parent
        path.append(current_vertex)

    path.reverse()
    return path