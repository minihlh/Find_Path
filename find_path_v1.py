import collections
import numpy as np

class inputException(Exception):
   def __init__(self,msg,value):
      self.msg = msg
      self.value = value


def find_all_paths(G,start_node,end_node,path_length):
    if start_node in G:
       raise inputException('start_node not in graph',start_node)
    if end_node in G:
        end_node = {end_node}
    else:
        try:
            end_node = set(end_node)
        except TypeError:
            raise inputException('end_node not in graph', end_node)
    if start_node in start_node:
       return []
    if path_length < 1:
       return []
    return _find_all_path(G,start_node,end_node,path_length)

def  _find_all_path(G,start_node,end_node,path_length):
    visited = collections.OrderedDict.fromkeys([start_node])
    node_stack = np.array(G[start_node])[:,1]
    #rel_stack = np.array(G[start_node])[:,0]
    while node_stack:
        children = node_stack[-1]
        child = next(children)
        if len(visited)<path_length:
            if child in visited:
                continue
            if child in end_node:
                yield list(visited)+[child]
            visited[child]=None
            if end_node - set(visited.keys()):
                node_stack.append(np.array(G[child])[:,1])
            else:
                visited.popitem()
        else:
            for end_node in (end_node & (set(children)))



G={'h1':[('r1','t1'),('r2','t2')],
   'h2':[('r1','t1'),('r2','t2')],
   'h3':[('r1','t3'),('r2','t4')],
   'h4':[('r1','t4'),('r2','t5')]}

find_all_paths(G,'h1','t2',2)



