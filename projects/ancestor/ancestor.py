from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    added = []
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

    # to find the earliest ancestor, 
    # find the parent node where the starting_node is in the set
    # repeat with the parent node until current node no longer has parents

    current_earliest = None
    node = starting_node
    hasParents = True
    
    while hasParents:
        for parent in graph.vertices: 
            if node in graph.vertices[parent]:
                current_earliest = parent
                node = parent
        hasParents = False
    
    print(current_earliest)
    return current_earliest or -1