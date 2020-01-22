from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    # make a graph inserting all of the ancestors
    for parent, child in ancestors:
        graph.add_vertex(parent)
        graph.add_vertex(child)
    
    for parent, child in ancestors:
        graph.add_edge(parent, child)

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
