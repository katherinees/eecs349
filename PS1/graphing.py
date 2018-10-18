import matplotlib.pyplot as plt
import ID3, parse, random

inFile = 'house_votes_84.data'
data = parse.parse(inFile)
k = 10
def calc(i):
    no_prune = 0
    w_prune = 0
    for j in range(100):
        random.shuffle(data)
        train = data[:i]
        # print(len(data))
        test_index = i+1+(len(data)-i)//2
        # print(test_index)
        test = data[i+1:test_index]
        valid = data[test_index:]
        tree = ID3.ID3(train, 'democrat')
        # tree.get_info()
        no_prune += ID3.test(tree, test)
        ID3.prune(tree, valid)
        w_prune += ID3.test(tree, test)
    return [float(no_prune)/float(100), float(w_prune)/float(100)]

no_p = []
w_p = []
x_axis = []
for i in range(10, 300, 1):
    res = calc(i)
    no_p.append(res[0])
    w_p.append(res[1])
    x_axis.append(i)

plt.plot(x_axis, no_p, 'r--', x_axis, w_p, 'b--')
plt.legend('without pruning', 'with pruning')
plt.show()

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
