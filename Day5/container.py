
# ------------------- Part A -------------------
# Build an array of array of the containers. 
def buildContainer(lines):
    # Slice relevent part of the array
    allContainer = lines[:8]
    allContainer.reverse()
    # Create attay with 9 other empty arrays inside
    finalContainer = [ [] for _ in range(9) ]

    for i in allContainer:
        # Access every location of the data, avoiding other chars
        for count, j in enumerate(range(1, len(i), 4)):
            # I there is a char on the spot, we add that to an array
            if i[j] != " ":
                finalContainer[count] += i[j]

    return finalContainer


def rebuildContainer(container, instruction):
    word = ""
    for i in instruction:
        # split the data and extract int
        i = i.split(" ")
        amount, source, destination = int(i[1]), int(i[3]) - 1, int(i[5]) - 1
        # Pop amount from source and append to destination
        for _ in range(amount):
            container[destination] += container[source].pop()
    
    # Adding all the top chars together
    for i in range(9):
        word += container[i][-1]

    print(word)

def rebuild2(container, instruction):
    word = ""
    print(len(instruction))
    for i in instruction:
        i = i.split(" ")
        amount, source, destination = int(i[1]), int(i[3]) - 1, int(i[5]) - 1

        # Splitting the array and adding to destination, and setting new to source
        container[destination] += container[source][-amount:]
        container[source] = container[source][:-amount]
    
    for i in range(9):
        word += container[i][-1]
    print(word)
    return word

def main():
    with open('./Day5/input.txt') as f:
        instructBegins = 11
        # Every row into array
        lines = f.readlines()
        container = buildContainer(lines)
        # Part A Un comment for print
        #rebuildContainer(container, lines[10:])

        # Part B
        rebuild2(container, lines[10:])



main()