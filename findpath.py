def findAllPath(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    paths = []  # 存储所有路径
    for node in graph[start]:
        if node not in path:
            #newpaths = []
            newpath = findAllPath(graph, node, end, path)
            for newpath in newpath:
                paths.append(newpath)

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    # if start not in graph:
    #     return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def find_all_paths(graph, start, end, path=[]):
    # if k<0:
    #     if end in path:
    #         return [path]
    #     else:
    #         exit()
    # else:
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


graph = {'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C'],
        'E': ['F'],
        'F': ['E', 'C']}

allpath = find_all_paths(graph, 'A', 'C')
#allpath = find_path(graph, 'B', 'F')
print('\n所有路径：', allpath)


