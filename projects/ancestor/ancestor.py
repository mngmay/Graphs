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

    # to find the earliest ancestor, 
    # find the parent node where the starting_node is in the set
    # repeat with the parent node until current node no longer has parents
    
    stack = Stack()
    
    def find_earliest(node):    
        for parent in graph.vertices: 
            if node in graph.vertices[parent]:
                stack.push(parent)
        if stack.size() < 1:
            if node != starting_node:
                return node
            else:
                return -1
        new_node = stack.pop()
        return find_earliest(new_node)
    
    return find_earliest(starting_node)
