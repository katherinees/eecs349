import ID3, parse, random, unit_tests
import pprint, copy
# data = [dict(a=1, b=0, Class='Dem'), dict(a=0, b=0, Class='Rep'), dict(a=1, b=1, Class='Rep')]
# tree = ID3.ID3(data, 0)
# tree.get_info()

data = [dict(a=0, b=1, c=0, Class=1), dict(a=1, b=1, c=1, Class=1), dict(a=1, b=1, c=0, Class=0), dict(a=1, b=0, c=1, Class=0)]
data.append(dict(a=0, b=1, c=1, Class=1))
x = ID3.gain('b', data)
# print(x) # expect 0.64902249
y = ID3.gain('a', data)
# print(y) # expect 0.55097750

# ID3.pick_split(data)

tree = ID3.ID3(data, 0)
tree.get_info()
print('\n')
x = ID3.prune(tree, [dict(a=0, b=1, c=0, Class=0), dict(a=0, b=1, c=0, Class=1), dict(a=0, b=1, c=0, Class=1)])
tree.children['a:0'].get_info()
# x[1].get_info()
# tree2 = copy.deepcopy(tree)
# tree2.label = 'no'
# tree.get_info()
# tree2.get_info()

# tree.children['a:1'].children['b:1'].children['c:1'].get_info()
# tree.children['a:0'].get_info()
# tree.get_info()
# tree.children[1].get_info()
# tree.children[0].get_info()
# tree.children[1].children[0].get_info()
# tree.children[1].children[0].children[0].get_info()
# pprint.pprint(ID3.partition('a', data))
# print('h', ID3.test(tree, [dict(a=0, b=1, c=1, Class=1), dict(a=0, b=1, c=1, Class=0)]))

unit_tests.testPruningOnHouseData('house_votes_84.data')
