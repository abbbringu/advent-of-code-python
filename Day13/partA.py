import json
import builtins
pairs = []

# Build our and sort our data
with open('./Day13/input.txt') as f:
    lines = f.readlines()
    pair = []
    for line in lines:
        if line == "\n":
            pairs.append(pair)
            pair = []
        else:
            line = line.strip()
            pair.append(json.loads(line))

# Pairwise comparisons.
def comp(left, right) -> int:
    while left and right:
        # If both are ints
        l = left.pop(0)
        r = right.pop(0)
        if type(l) == type(r) == builtins.int:
            if l < r:
                return 1
            elif l > r:
                return -1
            else: return 0
        elif type(l) == type(r) == builtins.list:
            val = comp(l, r)
            if val:
                return val
            
        elif type(l) == builtins.int:
            val = comp([l], r)
            if val:
                return val
        else:
            val = comp(l, [r])
            if val:
                return val
    return (1 if (len(left) - len(right)) <= 0 else -1)
    

# Loops through all paris
index = 1
correct = []
for pair in pairs:
    left, right = pair[0], pair[1]
    if comp(left, right) == 1:
        correct.append(index)
    index += 1
print(sum(correct))

