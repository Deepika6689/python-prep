# import copy
# hero={"name":"deepika",
#       "addr":{"resi":"glb",
#               "perm":"btm"}}
# print(hero)
# h1=hero.copy()
# h2=copy.deepcopy(hero)
# hero["addr"]["perm"]="majestic"
# print(hero)
# print(h1)
# print(hero)
# print(h2)

# {'name': 'deepika', 'addr': {'resi': 'glb', 'perm': 'btm'}}
# {'name': 'deepika', 'addr': {'resi': 'glb', 'perm': 'majestic'}}
# {'name': 'deepika', 'addr': {'resi': 'glb', 'perm': 'majestic'}}
# {'name': 'deepika', 'addr': {'resi': 'glb', 'perm': 'majestic'}}
# {'name': 'deepika', 'addr': {'resi': 'glb', 'perm': 'btm'}}

# emp_id=[101,102,103,104]
# names=["shaky","rahul","rakshith","nehru"]
# res=dict(zip(names,emp_id))
# print(res) {'shaky': 101, 'rahul': 102, 'rakshith': 103, 'nehru': 104}
# mob =[11,420,840,7]
# addr=["pentagon","thailand","russia","india"]
# info=dict(zip(emp_id,names,mob,addr))
# print(info)---------->error
# res1=list(zip(names,mob,addr))
# final_info=dict(zip(emp_id,res1))
# print(final_info) ----->{101: ('shaky', 11, 'pentagon'), 102: ('rahul', 420, 'thailand'), 103: ('rakshith', 840, 'russia'), 104: ('nehru', 7, 'india')}





