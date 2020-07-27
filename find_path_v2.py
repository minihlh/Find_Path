import numpy as np
import collections

def traverse(start,end,cutlength,path=[]):
    #main_stack = [start]
    side_stack = np.array(G[start])[:,1] #保存邻居节点
    #side_stack = G[start] 将关系也直接入栈
    visited = collections.OrderedDict([start])#记录走过的路径

    while side_stack:
        side_top = side_stack.pop()
        if len(visited)<cutlength:
            if side_top in visited:
                continue
            if side_top in end:
                list(visited).append(side_top)
            visited[side_top]=None
            temp_stack = np.array(G[side_top])[:, 1]
            if len(temp_stack)>0:
                side_top=[]
                for v in temp_stack: #将没有走过的邻居节点存进去
                    if v not in main_stack:
                        side_top.append(v)
                side_stack.append(side_top)
            else:
                main_stack.pop()

            if len(main_stack)>0 and main_stack[-1] ==end:
                pop_stack(main_stack, side_stack,path)
        #else:

def pop_stack(main_stack,side_stack,path):
    path.append(main_stack.pop())
    if len(side_stack)>0:
        side_stack.pop()







G={'h1':[['r1','t1'],['r2','t2']],
   'h2':[['r1','t1'],['r2','t2']],
   'h3':[['r1','t3'],['r2','t4']],
   'h4':[['r1','t4'],['r2','t5']]}