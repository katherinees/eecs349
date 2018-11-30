import csv
import random
import numpy as np

# with open('ps4.csv', 'w') as output:
#     writer = csv.writer(output)
#     writer.writerow(['a', 'class'])
#     for i in range(0, 1000):
#         writer.writerow([i, 'a' if i%2==0 else 'b'])

with open('ps4p2.csv', 'w') as output:
    writer = csv.writer(output)
    writer.writerow(['a', 'b', 'c', 'd', 'e', 'class'])
    for i in range(0, 1000):
        x = random.randint(0, 1)
        y = random.randint(0, 1)
        z1 = random.randint(0, 100)
        z2 = random.randint(0, 100)
        z3 = random.randint(0, 100)
        writer.writerow([x, y, z1, z2, z3, x != y])
