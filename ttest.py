# from itertools import *
# tt=[['aa', ['b', 'd'], 'cc'], ['aa', ['d'], 'pp', ['a'], 'cc']]
# # print(len(tt[0]))
# tc=['aa','cc','dd','ff']
# rr=[['b','c'],['d','e'],['f','g']]
# dd=['cc']
# rrr=['d','f']
# ddd=['dd']
# l=len(tc)
#
# # temp=[d for d in product([tc[0]],rr[0],[tc[1]])]
# d=product([[1,2],[3,4]],[5,6])
# for i in [1,2]:
#     temp=[d for d in product(temp,rr[i],[tc[i+1]])]
#     # temppp=[d for d in product(tempp,rr[2],[tc[3]])]
# print(temp)
# temptemp=[r for r in product(temp,rr,rr)]

# print(temptemp)

# [(('aa', 'b', 'cc'), 'b', 'b'), (('aa', 'b', 'cc'), 'b', 'c'), (('aa', 'b', 'cc'), 'c', 'b'), (('aa', 'b', 'cc'), 'c', 'c'), (('aa', 'c', 'cc'), 'b', 'b'), (('aa', 'c', 'cc'), 'b', 'c'), (('aa', 'c', 'cc'), 'c', 'b'), (('aa', 'c', 'cc'), 'c', 'c')]
# [((('aa', 'b', 'cc'), 'd', 'dd'), 'f', 'ff'), ((('aa', 'b', 'cc'), 'd', 'dd'), 'g', 'ff'), ((('aa', 'b', 'cc'), 'e', 'dd'), 'f', 'ff'), ((('aa', 'b', 'cc'), 'e', 'dd'), 'g', 'ff'), ((('aa', 'c', 'cc'), 'd', 'dd'), 'f', 'ff'), ((('aa', 'c', 'cc'), 'd', 'dd'), 'g', 'ff'), ((('aa', 'c', 'cc'), 'e', 'dd'), 'f', 'ff'), ((('aa', 'c', 'cc'), 'e', 'dd'), 'g', 'ff')]
# /m/04nrcg	/sports/sports_team/roster./soccer/football_roster_position/position	/m/02sdk9v
# /m/04nrcg	/soccer/football_team/current_roster./soccer/football_roster_position/position	/m/02sdk9v
# /m/04nrcg	/soccer/football_team/current_roster./sports/sports_team_roster/position	/m/02sdk9v
# /m/04nrcg	/sports/sports_team/roster./sports/sports_team_roster/position	/m/02sdk9v
#
# /m/02sdk9v	/sports/sports_position/players./sports/sports_team_roster/team	/m/04nrcg
# /m/02sdk9v	/sports/sports_position/players./soccer/football_roster_position/team	/m/04nrcg
