def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)

def depth_first_search_another_example():
    graph = {
        'X': ['Y', 'Z'],
        'Y': ['W', 'V'],
        'Z': ['U'],
        'W': [],
        'V': ['U'],
        'U': []
    }
    
    dfs_recursive(graph, 'X')


depth_first_search_another_example()
