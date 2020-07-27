import numpy as np

def fp(G, start, end, length):
    all_path =[]
    visit = [start]
    #stack = np.append((G[start])[:,1])
    stack = [G[start]]
    while stack:
        child = stack[-1]
        if len(child)>0:
            if len(visit)<length:
                if child == end:
                    stack.pop()
                    all_path.append(visit.append(child))
                    visit.pop()
                if child not in visit:
                    stack.pop()
                    visit.append(child)
                    stack.append(G[child])
        else:
            stack.pop()
graph = {'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C'],
        'E': ['F'],
        'F': ['E', 'C']}

allpath = fp(graph, 'A', 'C',3)
