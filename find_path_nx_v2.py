import collections
import numpy as np
import pandas as pd
from itertools import *
from collections import defaultdict
class inputException(Exception):
   def __init__(self,msg,value):#报错
      self.msg = msg
      self.value = value
def all_simple_paths(G, source, target, cutoff=None):
    if source not in G: #如果头节点不在图中，报错
        raise inputException('source node not in graph' ,source)
    if target in G: #如果尾节点在图中，变为一个字典
        targets = {target}
    else: #如果不在图中，则报错
        try:
            targets = set(target)
        except TypeError:
            raise inputException('target node not in graph' , target)
    if source in targets: #如果头节点等于尾节点，返回空列表
        return []
    if cutoff < 1:#如果输入长度小于1，返回空
        return []
    return _all_simple_paths_graph(G, source, targets, cutoff) #开始查找路径
def _all_simple_paths_graph(G, source, targets, cutoff):
    visited = collections.OrderedDict.fromkeys([source]) #记录走过的节点
    stack = [iter(G[source])] #迭代器的用法不知道，不是很理解为什么要用iter
    while stack: #
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.popitem()
        elif len(visited) < cutoff:
            if child in visited:
                continue
            if child in targets:
                yield list(visited) + [child]
            visited[child] = None
            if targets - set(visited.keys()):  # expand stack until find all targets
                stack.append(iter(G[child]))
            else:
                visited.popitem()  # maybe other ways to child
        else:  # len(visited) == cutoff:
            for target in (targets & (set(children) | {child})) - set(visited.keys()):
                yield list(visited) + [target]
            stack.pop()
            visited.popitem()

df = pd.read_csv(r"train.txt",encoding='utf-8',sep='\\s+',names=['h','r','t'])
data = np.array(df)
graph_dict = defaultdict(dict)
graph_realtion_dict=defaultdict(list)
for key,value,relation in zip(data[:,0],data[:,2],data[:,1]):
    graph_dict[key][value]={}
    graph_dict[value][key] = {}
    graph_realtion_dict[key].append([value,relation,0])
    graph_realtion_dict[value].append([key,relation,1])
all_temp_path=list(all_simple_paths(graph_dict,'Kafka','系统网络异常',cutoff=2))
print("path is",all_temp_path)
all_path=[]
for path in all_temp_path:
    path_r_list=[]
    for i in range(len(path)-1):
        neibor_list=np.array(graph_realtion_dict[path[i]])
        node_index = np.where(neibor_list[:, 0] == path[i + 1])[0].tolist()
        r_list=[list(neibor_list[j,[1,2]]) for j in node_index]
        # print(r_list)
        path_r_list.append(r_list)
    temp = [d for d in product([path[0]], path_r_list[0], [path[1]])]
    for i in range(1,len(path)-1):
        temp = [d for d in product(temp, path_r_list[i], [path[i + 1]])]
    temp_path=[[str(temp[i]).replace("(", "").replace(")", "")] for i in range(len(temp))]
    all_path.append(temp_path)
print(all_path)


# itertools函数
# starmap针对list中的每一项调用函数，starmap（fun，list）

# df[df.iloc[:,0]=='path[i+1]']
# for path in all_temp_path:
#     for i in range(len(path)):
#         end_node=np.array(graph_realtion_dict[path[i]])
#         node_index=np.where(end_node[:,1]==path[i+1])
#         for j in node_index:
#             relation=end_node[i][1]
#             paths=path[i]+[relation]
# pd.concat([tff,cccc],axis=1)
# df.groupby('h')['t'].apply(lambda x:','.join(x)).to_frame()
# df.groupby(["h","t"])["r"].apply(lambda x:','.join(x)).to_frame()
# G={0: {1: {}, 2: {}, 4: {}}, 1: {0: {}, 2: {}, 3: {}}, 2: {0: {}, 1: {}, 3: {}}, 3: {1: {}, 2: {}}, 4: {0: {}}}
# G={0: {1, 2, 4}, 1: {0, 2, 3}, 2: {0, 1, 3}, 3: {1, 2}, 4: {0}}

# [[('/m/04nrcg', '/soccer/football_team/current_roster./soccer/football_roster_position/position', '/m/02sdk9v'),
# ('/m/04nrcg', '/soccer/football_team/current_roster./sports/sports_team_roster/position', '/m/02sdk9v'),
# ('/m/04nrcg', '/sports/sports_team/roster./sports/sports_team_roster/position', '/m/02sdk9v'),
# ('/m/04nrcg', '/sports/sports_team/roster./soccer/football_roster_position/position', '/m/02sdk9v')],
# [(('/m/04nrcg', '/soccer/football_team/current_roster./sports/sports_team_roster/position', '/m/02nzb8'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/sports/sports_team/roster./sports/sports_team_roster/position', '/m/02nzb8'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/soccer/football_team/current_roster./soccer/football_roster_position/position', '/m/02nzb8'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/sports/sports_team/roster./soccer/football_roster_position/position', '/m/02nzb8'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v')],
# [(('/m/04nrcg', '/sports/sports_team/roster./soccer/football_roster_position/position', '/m/02_j1w'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/sports/sports_team/roster./sports/sports_team_roster/position', '/m/02_j1w'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/soccer/football_team/current_roster./sports/sports_team_roster/position', '/m/02_j1w'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/soccer/football_team/current_roster./soccer/football_roster_position/position', '/m/02_j1w'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v')],
# [(('/m/04nrcg', '/sports/sports_team/roster./sports/sports_team_roster/position', '/m/0dgrmp'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/sports/sports_team/roster./soccer/football_roster_position/position', '/m/0dgrmp'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/soccer/football_team/current_roster./sports/sports_team_roster/position', '/m/0dgrmp'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v'),
# (('/m/04nrcg', '/soccer/football_team/current_roster./soccer/football_roster_position/position', '/m/0dgrmp'), '/sports/sports_position/players./sports/sports_team_roster/position', '/m/02sdk9v')]]

# [[('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02sdk9v'),
#   ('/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02sdk9v'),
#   ('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   ('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   ('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02sdk9v'),
#   ('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02sdk9v')],
#  [(('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02nzb8'),  ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02nzb8'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v')],
#  [(('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02_j1w'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v')],
#  [(('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'),
#   (('/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/0dgrmp'), ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v')]]


# [["'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02sdk9v'",
#   "'/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02sdk9v'",
#   "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02sdk9v'",
#   "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02sdk9v'",
#   "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02sdk9v'",
#   "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02sdk9v'"],
#  ["'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02nzb8', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'"], ["'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/02_j1w', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'"], ["'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_team/roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./soccer/football_roster_position/team', '1'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./sports/sports_team_roster/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/soccer/football_team/current_roster./soccer/football_roster_position/position', '0'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '0'], '/m/02sdk9v'", "'/m/04nrcg', ['/sports/sports_position/players./sports/sports_team_roster/team', '1'], '/m/0dgrmp', ['/sports/sports_position/players./sports/sports_team_roster/position', '1'], '/m/02sdk9v'"]]


# [[('aa', ['b', '0'], 'cc'), ('aa', ['d', '0'], 'cc'), ('aa', ['t', '1'], 'cc')],[(('aa', ['d', '0'], 'pp'), ['a', '0'], 'cc'), (('aa', ['d', '0'], 'pp'), ['d', '0'], 'cc')]]

# [["'aa', ['b', '0'], 'cc'", "'aa', ['d', '0'], 'cc'", "'aa', ['t', '1'], 'cc'"], ["'aa', ['d', '0'], 'pp', ['a', '0'], 'cc'", "'aa', ['d', '0'], 'pp', ['d', '0'], 'cc'"]]

# [["'Kafka', ['包含', '0'], 'Consumer', ['不消费', '0'], '系统网络异常'",
# "'Kafka', ['包含', '0'], 'Consumer', ['消费失败', '0'], '系统网络异常'",
# "'Kafka', ['包含', '0'], 'Consumer', ['不消费', '0'], '系统网络异常'",
# "'Kafka', ['包含', '0'], 'Consumer', ['消费失败', '0'], '系统网络异常'",
# "'Kafka', ['不消费', '1'], 'Consumer', ['不消费', '0'], '系统网络异常'",
# "'Kafka', ['不消费', '1'], 'Consumer', ['消费失败', '0'], '系统网络异常'",
# "'Kafka', ['不消费', '1'], 'Consumer', ['不消费', '0'], '系统网络异常'",
# "'Kafka', ['不消费', '1'], 'Consumer', ['消费失败', '0'], '系统网络异常'"],
# ["'Kafka', ['关联', '1'], 'HDFS', ['写操作失败', '0'], '系统网络异常'"],
# ["'Kafka', ['关联', '0'], 'DataCollectors', ['数据消费失败', '0'], '系统网络异常'",
# "'Kafka', ['关联', '0'], 'DataCollectors', ['消费堆积', '0'], '系统网络异常'",
# "'Kafka', ['依赖', '1'], 'DataCollectors', ['数据消费失败', '0'], '系统网络异常'",
# "'Kafka', ['依赖', '1'], 'DataCollectors', ['消费堆积', '0'], '系统网络异常'",
# "'Kafka', ['数据消费失败', '1'], 'DataCollectors', ['数据消费失败', '0'], '系统网络异常'",
# "'Kafka', ['数据消费失败', '1'], 'DataCollectors', ['消费堆积', '0'], '系统网络异常'",
# "'Kafka', ['数据消费失败', '1'], 'DataCollectors', ['数据消费失败', '0'], '系统网络异常'",
# "'Kafka', ['数据消费失败', '1'], 'DataCollectors', ['消费堆积', '0'], '系统网络异常'",
# "'Kafka', ['消费堆积', '1'], 'DataCollectors', ['数据消费失败', '0'], '系统网络异常'",
# "'Kafka', ['消费堆积', '1'], 'DataCollectors', ['消费堆积', '0'], '系统网络异常'"],
# ["'Kafka', ['关联', '0'], 'Producer', ['发送消息超时', '0'], '系统网络异常'",
# "'Kafka', ['关联', '0'], 'Producer', ['发送消息失败', '0'], '系统网络异常'",
# "'Kafka', ['包含', '0'], 'Producer', ['发送消息超时', '0'], '系统网络异常'",
# "'Kafka', ['包含', '0'], 'Producer', ['发送消息失败', '0'], '系统网络异常'"],
# ["'Kafka', ['依赖', '1'], 'UDE', ['节点切换频繁', '0'], '系统网络异常'"],
# ["'Kafka', ['关联', '0'], '系统', ['故障所属', '1'], '系统网络异常'",
# "'Kafka', ['关联', '1'], '系统', ['故障所属', '1'], '系统网络异常'"],
# ["'Kafka', ['故障所属', '1'], 'Kafka连接ZooKeeper异常', ['导致', '0'], '系统网络异常'",
# "'Kafka', ['服务异常下线', '0'], 'Kafka连接ZooKeeper异常', ['导致', '0'], '系统网络异常'"],
# ["'Kafka', ['故障所属', '1'], 'Kafka服务异常', ['导致', '0'], '系统网络异常'",
# "'Kafka', ['CPU使用率过高', '0'], 'Kafka服务异常', ['导致', '0'], '系统网络异常'",
# "'Kafka', ['GC时间长', '0'], 'Kafka服务异常', ['导致', '0'], '系统网络异常'",
# "'Kafka', ['消费慢', '0'], 'Kafka服务异常', ['导致', '0'], '系统网络异常'"],
# ["'Kafka', ['依赖', '0'], 'ZooKeeper', ['服务异常', '0'], '系统网络异常'",
# "'Kafka', ['异常重启', '0'], 'ZooKeeper', ['服务异常', '0'], '系统网络异常'",
# "'Kafka', ['关联', '1'], 'ZooKeeper', ['服务异常', '0'], '系统网络异常'"],
# ["'Kafka', ['服务异常', '0'], 'ZooKeeper服务异常', ['导致', '1'], '系统网络异常'",
# "'Kafka', ['连接ZooKeeper异常', '0'], 'ZooKeeper服务异常', ['导致', '1'], '系统网络异常'"],
# ["'Kafka', ['ISR不可用', '0'], '系统网络异常'",
# "'Kafka', ['数据写入失败', '0'], '系统网络异常'",
# "'Kafka', ['重复消费', '0'], '系统网络异常'",
# "'Kafka', ['消费异常', '0'], '系统网络异常'"]]

# [['Kafka', 'Consumer', '系统网络异常'],
#  ['Kafka', 'HDFS', '系统网络异常'],
#  ['Kafka', 'DataCollectors', '系统网络异常'],
#  ['Kafka', 'Producer', '系统网络异常'],
#  ['Kafka', 'UDE', '系统网络异常'],
#  ['Kafka', '系统', '系统网络异常'],
#  ['Kafka', 'Kafka连接ZooKeeper异常', '系统网络异常'],
#  ['Kafka', 'Kafka服务异常', '系统网络异常'],
#  ['Kafka', 'ZooKeeper', '系统网络异常'],
#  ['Kafka', 'ZooKeeper服务异常', '系统网络异常'],
#  ['Kafka', '系统网络异常']]
