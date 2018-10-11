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
        print('examples is empty')
        return tree
    else:
        root = Node()
        return ID3_helper(examples, root)


def ID3_helper(examples, root):
    print('all same class?', all_same_class(examples))
    if all_same_class(examples):
        root.leaf = True
        root.value = examples[0]['Class']
        return root
    print('only trivial splits possible?', only_trivial_splits(examples))
    if only_trivial_splits(examples):
        root.leaf = True
        root.value = find_mode_class(examples)
        return root
    print('then it\'s time to get s p l i t y')
    return root

def pick_split(examples):
    attributes = list(examples[0].keys())
    attributes.remove('Class')
    info_gain = {}
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


def evaluate(node, example):
  '''
  Takes in a tree and one example.  Returns the Class value that the tree
  assigns to the example.
  '''
