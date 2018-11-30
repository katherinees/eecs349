import os

girl_names = set()
boy_names = set()

directory = 'names'
for f in os.listdir(directory):
    path = directory + "/" + f
    yob = open(path, "r")
    for line in yob:
        line = line.split(",")
        if line[1] == "F":
            girl_names.add(line[0])
        else:
            boy_names.add(line[0])
