# import pandas as pd
# edg_list = [['B', 'C'],['C', 'B'],
#            ['A', 'B'],['B', 'A'],
#             ['A', 'C'], ['C', 'A'],
#             ['C', 'D'], ['D', 'C']]
# pd_edg_list = pd.DataFrame(edg_list,columns=[1,2])
# # edg_dict1 = pd.DataFrame({'key':['B', 'C', 'A', 'B', 'A', 'C', 'C', 'D'],'date':['C','B', 'B', 'A', 'C', 'A', 'D', 'C']})
# # edg_dict2 = pd.DataFrame({'key':['B', 'C', 'A', 'B', 'A', 'C', 'C', 'D'],'value':['C','B', 'B', 'A', 'C', 'A', 'D', 'C']})
# edg_dict1 = pd.DataFrame({'key':['B', 'C', 'A', 'B', 'A', 'C', 'C', 'D'],'date':['C','B', 'B', 'A', 'C', 'A', 'D', 'C']})
# edg_dict2 = pd.DataFrame({'key':['C','B', 'B', 'A', 'C', 'A', 'D', 'C'],'value':['B', 'C', 'A', 'B', 'A', 'C', 'C', 'D']})
# #result = pd.merge(left=pd_edg_list, right=pd_edg_list)
# #pd_edg_list.set_index(0).join(pd_edg_list.set_index(1))
# #print(pd_edg_list.values)
# #print(pd_edg_list.join(pd_edg_list, lsuffix='_left', rsuffix='_right'))
# #print(pd_edg_list)
# print(pd.merge(edg_dict1,edg_dict2, on=['key'], how='left'))


# def traverse(start, end):
#     main_stack = [start]
#     side_stack = [map[start]]
#
#     while len(main_stack) > 0:
#         side_top = side_stack.pop()#弹出最近的邻居列表
#         if len(side_top) > 0:#判断是否有邻居
#             main_top = side_top[0] #取邻居列表的第一个邻居
#             main_stack.append(main_top) #加入到主栈中
#             side_stack.append(side_top[1:]) #将其余元素压入辅助栈中
#             if len(map[main_top]) > 0: #判断是否有邻居节点
#                 side_top = []
#                 for v in map[main_top]: #对邻居节点判断是否在路径中
#                     if v not in main_stack: #如果不在，将该节点加入辅助栈中
#                         side_top.append(v)
#                 side_stack.append(side_top)
#         else: #如果没有邻居，则直接弹出
#             main_stack.pop()
#
#         if len(main_stack) > 0 and main_stack[-1] == end:
#             #print("==============FOUND==============")
#             print(main_stack)
#             pop_stack(main_stack, side_stack)
#
# def pop_stack(main_stack, side_stack):
#     main_stack.pop()
#     if len(side_stack) > 0:
#         side_stack.pop()

map = {
    'V0': ['V1', 'V2'],
    'V1': ['V0', 'V3', 'V4'],
    'V2': ['V0', 'V5', 'V6'],
    'V3': ['V1', 'V7'],
    'V4': ['V1', 'V5', 'V7'],
    'V5': ['V2', 'V4', 'V6'],
    'V6': ['V2', 'V5', 'V8'],
    'V7': ['V3', 'V4'],
    'V8': ['V6']
}

# if __name__ == '__main__':
#     traverse('V3', 'V6')




def find_all_paths(graph, start, end):
    path  = []
    paths = []
    queue = [(start, end, path)]
    while queue:
        start, end, path = queue.pop()
        print('PATH', path)

        path = path + [start]
        if start == end:
            paths.append(path)
        for node in set(graph[start]).difference(path):
            queue.append((node, end, path))
    return paths

graph = {'A': ['B', 'C'],
        'B': ['A', 'C', 'D'],
        'C': ['A', 'B', 'D', 'F'],
        'D': ['B', 'C'],
        'E': ['F'],
        'F': ['E', 'C']}

allpath = find_all_paths(graph, 'A', 'C')
print('\n所有路径：', allpath)