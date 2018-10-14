from node import Node
import math

def ID3(examples, default):
    '''
    Takes in an array of examples, and returns a tree (an instance of Node)
    trained on the examples.  Each example is a dictionary of attribute:value pairs,
    and the target class variable is a special attribute with the name "Class".
    Any missing attributes are denoted with a value of "?"
    '''
    if len(examples) == 0:
        tree = Node()
        tree.leaf = True
        tree.value = default
        # print('examples is empty')
        return tree
    else:
        root = Node()
        root.label = 'TreeRoot'
        root.freq = len(examples)
        first_split = pick_split(examples)
        poss_v = set()
        for e in examples:
            poss_v.add(e[first_split])
        branches = partition(first_split, examples)
        for b in branches:
            new_root = Node()
            new_root.label = first_split + ':' + str(branches[b][0][first_split])
            root.children[new_root.label] = new_root
            ID3_helper(branches[b], new_root)
        return root

def ID3_helper(examples, root):
    root.freq = len(examples)
    # print('all same class?', all_same_class(examples))
    if all_same_class(examples):
        root.leaf = True
        root.value = examples[0]['Class']
        # root.freq = len(examples)
        return root
    # print('only trivial splits possible?', only_trivial_splits(examples))
    if only_trivial_splits(examples):
        root.leaf = True
        root.value = find_mode_class(examples)
        # root.freq = len(examples)
        return root
    # print('then it\'s time to get s p l i t t y')
    split_att = pick_split(examples)
    # print('we\'ll split on', split_att)
    # root.label = str(split_att)
    branches = partition(split_att, examples)
    # pprint.pprint(branches)
    for b in branches:
        # print('41', branches[b])
        # print('54', branches[b][0][split_att])
        new_root = Node()
        new_root.label = split_att + ':' + str(branches[b][0][split_att])
        root.children[new_root.label] = new_root
        ID3_helper(branches[b], new_root)
    return root

def partition(attribute, examples):
    partitions = {}
    for e in examples:
        if str(e[attribute]) not in partitions:
            partitions[str(e[attribute])] = [e]
        else:
            partitions[str(e[attribute])].append(e)
    return partitions

def entropy(vals):
    # takes array of ints
    ans = 0
    total = float(sum(vals))
    for v in vals:
        v = float(v)/total
        if v != 0:
            ans += v*math.log(v, 2)
    ans *= -1
    return ans

def gain(attribute, examples):
    av = {}
    num_examples = len(examples)
    running_sum = 0
    for e in examples:
        if str(e[attribute]) not in av:
            av[str(e[attribute])] = dict(has_att = 1, classes={})
        else:
            av[str(e[attribute])]['has_att'] += 1
    for ex in examples:
        c = str(ex['Class'])
        cur_att_val = str(ex[attribute])
        if c not in av[cur_att_val]['classes']:
            av[cur_att_val]['classes'][c] = 1
        else:
            av[cur_att_val]['classes'][c] += 1
        # print('58', av[cur_att_val])
    for v in av:
        p = float(av[v]['has_att'])/float(num_examples)
        # print('65', v, p)
        h_array = []
        for cl in av[v]['classes']:
            h_array.append(av[v]['classes'][cl])
            # print(v, cl, av[v]['classes'][cl])
        h = entropy(h_array)
        running_sum += p*h
    return(running_sum)

def pick_split(examples):
    # best split is on att w lowest gain
    attributes = list(examples[0].keys())
    attributes.remove('Class')
    # print(attributes)
    info_gain = {}
    for a in attributes:
        info_gain[a] = gain(a, examples)
    best_att = min(info_gain, key=info_gain.get)
    # print('85', best_att)
    return best_att
    # if max info gain is 0, prefer non trivial split

def find_mode_class(examples):
    classes = {}
    for e in examples:
        if str(e['Class']) not in classes:
            classes[str(e['Class'])] = 1
        else:
            classes[str(e['Class'])] += 1
    # print(classes)
    mode = max(classes, key=classes.get)
    print('the mode class is:', mode)
    return mode

def all_same_class(examples):
    classes = set()
    for e in examples:
        classes.add(e['Class'])
    if len(classes) == 1:
        return True
    else:
        return False

def only_trivial_splits(examples):
    attributes = list(examples[0].keys())
    attributes.remove('Class')
    adict = {}
    for a in attributes:
        adict[a] = set()
    for e in examples:
        for a in attributes:
            adict[a].add(e[a])
    # print(adict)
    only_trivial = True
    for s in adict:
        if len(adict[s]) > 1:
            only_trivial = False
    # print('there are only trivial splits:', only_trivial)
    return only_trivial

def prune(node, examples):
    '''
    Takes in a trained tree and a validation set of examples.  Prunes nodes in order
    to improve accuracy on the validation data; the precise pruning strategy is up to you.
    '''

def test(node, examples):
    '''
    Takes in a trained tree and a test set of examples.  Returns the accuracy (fraction
    of examples the tree classifies correctly).
    '''
    correct = 0
    for e in examples:
        tree_class = evaluate(node, e)
        if tree_class == e['Class']:
            correct += 1
    percent = float(correct)/float(len(examples))
    return(percent)

def evaluate(node, example):
    '''
    Takes in a tree and one example.  Returns the Class value that the tree
    assigns to the example.
    '''
    if node.leaf == True:
        return node.value
    else:
        poss_child = list(node.children.keys())
        split_att = poss_child[0].split(':')[0]
        if split_att in example:
            find_key = split_att + ':' + str(example[split_att])
            if find_key in poss_child:
                return evaluate(node.children[find_key], example)
            else:
                high_freq = {}
                for c in node.children:
                    high_freq[node.children[c].label] = node.children[c].freq
                good_enough = max(high_freq, key=high_freq.get)
                return evaluate(node.children[good_enough], example)
        else:
            high_freq = {}
            for c in node.children:
                high_freq[node.children[c].label] = node.children[c].freq
            good_enough = max(high_freq, key=high_freq.get)
            return evaluate(node.children[good_enough], example)
