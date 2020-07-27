def find_path(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node not in path:
            temppaths = find_path(graph, node, end, path)
            for temppath in temppaths:
                if len(temppath)<=5:
                    paths.append(temppath)
    return paths

graph = {'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C'],
        'E': ['F'],
        'F': ['E', 'C']}

allpath = find_path(graph, 'A', 'C')
print('\n所有路径：', allpath)