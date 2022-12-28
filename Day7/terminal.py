
# ------------------- Part A & B -------------------

def getSize(lines):
    data = []
    sizes = {}
    # Filter out uneccessary data
    for i in lines:
        row = i.split(" ")
        if (row[1] != 'ls\n' and row[0] != "dir"):
            data.append(row)
    
    # Go through the data

    stack = []
    for index in range(len(data)):
        line = data[index]
        if line[1] == "cd" and line[2] == '..\n':
            stack.pop()
        elif line[1] == "cd":
            stack.append(index)
            sizes[index] = 0
        else:
            size = int(line[0])
            for i in stack:
                sizes[i] += size

    values = sizes.values()
    #print(values)
    part1_answer = sum([sizes[i] for i in sizes if sizes[i] <= 100_000])

    memory = 70_000_000 - sizes[0]
    neededMemo = 30_000_000 - memory
    listOfAll = [sizes[i] for i in sizes if sizes[i] >= neededMemo]
    part2_answer = min(listOfAll)



    return (part1_answer, part2_answer)











def main():
    with open('./Day7/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        result = getSize(lines)
        print(f"Part A: {result[0]}")
        print(f"Part B: {result[1]}")

main()