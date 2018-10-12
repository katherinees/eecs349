class Node:
    def __init__(self):
        self.label = None
        self.children = {}
        self.leaf = False
        self.value = None
        self.freq = 0
	# you may want to add additional fields here...

    def get_info(self):
        print('Label:    ', self.label)
        print('Children: ', self.children)
        print('Leaf:     ', self.leaf)
        print('Value:    ', self.value)
        print('Frequency:', self.freq)
