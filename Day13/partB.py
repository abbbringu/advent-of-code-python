import json
pairs = []

# Build our and sort our data modified for B
with open('./Day13/input.txt') as f:
    lines = f.readlines()
    for line in lines:
        if line == "\n":
            continue
        else:
            line = line.strip()
            pairs.append(json.loads(line))

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

# The index is equal to the amount of items that are lower in pairs
index = 1
firstInd = 1 # 1 indexing
secondInd = 2 # considering first
first = [[2]]
second = [[6]]

for pkt in pairs:
    firstInd += (1 if comp(pkt, first) == 1 else 0)
    secondInd += (1 if comp(pkt, second) == 1 else 0)


print(firstInd*secondInd)

