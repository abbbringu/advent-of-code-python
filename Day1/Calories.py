
# ------------------- Part A -------------------
def findHeighest(lines: list):
    # Values for returning highest and for temp usage
    hi = 0
    temp = 0

    for i in lines:
        # If not new line, add to temp
        if i != "\n":
            temp += int(i)
        else:
            # new line is present, decide if we found a new high
            hi = hi if (hi > temp) else temp
            temp = 0

    return(hi)


# ------------------- Part B -------------------
def totalCalories(lines: list):
    # Look for top three elf with most calories 
    temp = 0
    topThree = [0,0,0] 

    for i in lines:
        # If not new line, add to temp
        if i != "\n":
            temp += int(i)
        else:
            # If temp is new all time heigh, we knock down the list and put temp on top
            if temp > topThree[0]:
                topThree[2], topThree[1], topThree[0] = topThree[1], topThree[0], temp
            # If temp is higher than current 2nd highest value 
            elif temp > topThree[1]:
                topThree[2], topThree[1] = topThree[1], temp
            # If temp is higher than current 3rd highest value 
            elif temp > topThree[2]:
                topThree[2] = temp
            temp = 0

    # Returning the sum of the top three caloreis bearer
    return(sum(topThree))



def main():
    # Access the file
    with open('./Day1/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        highest = findHeighest(lines)
        total = totalCalories(lines)
        print(f"Elf that carries to most: {highest} calories\nTop 3 Total Calories:     {total} calories")
        
main()