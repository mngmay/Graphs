from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    added = []
    print(graph)
    # make a graph inserting all of the ancestors
    for pair in ancestors:
        if pair[0] not in added:
            graph.add_vertex(pair[0])
            added.append(pair[0])
        if pair[1] not in added:
            graph.add_vertex(pair[1])
            added.append(pair[1])
        graph.add_edge(pair[0], pair[1])
    print("vertices", graph.vertices)

    for child in graph.vertices: 
        print(child)
    return -1