my_graph = {
    'Ashton':  [('Bodley', 4), ('Camby', 6), ('Darby', 5)],
    'Bodley':  [('Ashton', 4), ('Darby', 3), ('Talmon', 9)],
    'Camby':   [('Ashton', 6), ('Udisen', 4)],
    'Darby':   [('Bodley', 3), ('Ashton', 5), ('Elmont', 4), ('Foster', 7)],
    'Elmont':  [('Darby', 4), ('Foster', 3)],
    'Foster':  [('Elmont', 3), ('Darby', 7), ('Galton', 2), ('Iving', 6)],
    'Galton':  [('Foster', 2), ('Hemley', 4)],
    'Hemley':  [('Galton', 4), ('Iving', 3), ('Quimbly', 6)],
    'Iving':   [('Hemley', 3), ('Foster', 6), ('Jayston', 5), ('Kelvey', 8)],
    'Jayston': [('Iving', 5),  ('Kelvey', 6)],
    'Kelvey':  [('Jayston', 6), ('Iving', 8), ('Linnae', 2), ('Pernay', 9)],
    'Linnae':  [('Kelvey', 2),  ('Marfin', 4)],
    'Marfin':  [('Linnae', 4),  ('Pernay', 3)],
    'Pernay':  [('Marfin', 3),  ('Kelvey', 9), ('Quimbly', 5)],
    'Quimbly': [('Pernay', 5),  ('Hemley', 6), ('Serley', 4)],
    'Serley':  [('Quimbly', 4), ('Talmon', 7)],
    'Talmon':  [('Serley', 7),  ('Udisen', 3), ('Bodley', 9)],
    'Udisen':  [('Talmon', 3),  ('Welcot', 6), ('Camby', 4)],
    'Welcot':  [('Udisen', 6),  ('Yarath', 5)],
    'Yarath':  [('Welcot', 5)]
}

def shortest_path(graph: dict, start: str, target: str = '') -> tuple[dict, dict]:
    """
    Calculate the shortest path in a graph from a start node to a target node using Dijkstra's algorithm.
    Parameters:
    graph (dict): A dictionary representing the graph where keys are node names and values are lists of tuples (neighbor, distance).
    start (str): The starting node for the path calculation.
    target (str, optional): The target node for the path calculation. If not provided, the shortest paths to all nodes will be printed.
    Returns:
    tuple: A tuple containing two dictionaries:
        - distances (dict): A dictionary where keys are node names and values are the shortest distance from the start node.
        - paths (dict): A dictionary where keys are node names and values are lists representing the shortest path from the start node.
    """
    unvisited = list(graph)
    distances = {node: 0 if node == start else float('inf') for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)
    
    # While there are still unvisited nodes
    while unvisited:
        # Select the unvisited node with the smallest distance
        current = min(unvisited, key=distances.get)
        # For each neighbor of the current node
        for node, distance in graph[current]:
            # Calculate the new distance to the neighbor
            if distance + distances[current] < distances[node]:
                # Update the distance to the neighbor if it's shorter
                distances[node] = distance + distances[current]
                # Update the path to the neighbor
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        # Mark the current node as visited
        unvisited.remove(current)
    
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')
    
    return distances, paths
    
shortest_path(my_graph, 'Ashton', 'Quimbly')
