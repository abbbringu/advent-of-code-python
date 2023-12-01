import json
pairs = []

# Build our and sort our data
with open('./Day13/input.txt') as f:
    lines = f.readlines()
    pair = []
    for line in lines:
        # When new line, we append the pair and start a new one
        if line == "\n":
            pairs.append(pair)
            pair = []
        else:
            line = line.strip()
            pair.append(json.loads(line))

# Helper function for comp
def compare(l: int, r: int):
    if l < r:
        return 1
    elif l > r:
        return -1
    else:
        return 0

# Pairwise comparisons.
def comp(left, right) -> int:
    # we use switch case to determine how we handle the next compare 
    match left, right:
        case int(), int():
            return compare(left, right)
        case int(), list():
            return comp([left], right)
        case list(), int():
            return comp(left, [right])
        case list(), list():
            for l, r in zip(left, right):
                res = comp(l, r)
                if res != 0:
                    return res
            return comp(len(left), len(right))

# Loops through all paris
index = 1
correct = []
for pair in pairs:
    left, right = pair[0], pair[1]
    if comp(left, right) == 1:
        correct.append(index)
    index += 1
#print(sum(correct))

