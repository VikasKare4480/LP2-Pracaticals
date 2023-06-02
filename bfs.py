graph = {
    'A': ['B', 'C', 'E'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['A', 'B', 'D'],
    'F': ['C'],
    'G': ['C']
}

def bfs(graph, initial):
    visited = []
    queue = [initial]

    # Loop through the queue until it is empty
    while queue:
        # Pop the first element from the queue and assign it to the node variable
        node = queue.pop(0)

        # If the node has not been visited, add it to the visited list
        if node not in visited:
            visited.append(node)

        # Get the neighbors of the current node from the graph
        neighbors = graph[node]

        # Add the neighbors to the queue if they haven't been visited yet
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)

    # Return the visited list once all nodes have been explored
    return visited

# Call the bfs function with the graph and the initial node 'A', and print the result
print(bfs(graph, 'A'