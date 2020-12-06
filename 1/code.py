import numpy as np
from collections import deque
# read input
with open('1/input.txt') as file:
    lines = [line.rstrip() for line in file]

# convert to numeric
lines = np.array(list(map(int, lines)))

### PART 1
# subtract each number from 2020 and see if any of the results match another number in the list
differences = 2020-lines
pair_2020 = np.intersect1d(differences,lines)
result_1=pair_2020[0]*pair_2020[1]

### PART 2
# subtract every original number from every difference to get all possible combinations
differences_2 = differences-lines
for i in range(0, len(lines)):
    lines = deque(lines)
    lines.rotate(1)
    differences_2 = np.concatenate([differences_2, differences-lines])

# compare the differences with the original numbers to find the match
triplet_2020 = np.intersect1d(differences_2,lines)
result_2=triplet_2020[0]*triplet_2020[1]*triplet_2020[2]