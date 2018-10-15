import matplotlib.pyplot as plt
import ID3, parse, random

inFile = 'house_votes_84.data'
data = parse.parse(inFile)
k = 100
def calc(i):
    no_prune = 0
    for j in range(100):
        random.shuffle(data)
        train = data[:i]
        test = data[i+1:]
        tree = ID3.ID3(train, 'democrat')
        tree.get_info()
        no_prune += ID3.test(tree, test)
    return float(no_prune)/float(100)


print(calc(k))

# x_axis = []
# for i in range (10, 301):
#     x_axis.append(i)
#     no_prune = []
#     for j in range(100):
#         random.shuffle(data)
#         train = data[0:i]
#         test = data[i+1:]
#         tree = ID3.ID3(train, 'democrat')
#         no_prune.append(ID3.test(tree, test))
