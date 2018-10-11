import ID3, parse, random, unit_tests

data = [dict(a=1, b=0, Class=0), dict(a=1, b=0, Class=1), dict(a=1, b=1, Class=1)]
tree = ID3.ID3(data, 0)
tree.get_info()

# unit_tests.testID3AndEvaluate()
