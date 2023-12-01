
# ------------------- Part A -------------------
def sumOfDups(lines) -> int:
    # Used to calculate points
    points = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0

    # In this part, I avoided using array slicing for optimization 
    for i in lines:
        # -1 for accounting for \n in the strings
        length = len(i) -1
        half = (length) // 2
        found = False

        # Loop through each character¨
        for count, item in enumerate(i):
            if count == half:
                break
            # Check the other half of the string
            for look in range(0, half):
                if item == i[(length - 1 - look)]:
                    # Add score according to the rules
                    score += points.index(item) + 1
                    found = True
                    break
            # Break from keep searching in the word  
            if found:
                found = False
                break
    return score

# ------------------- Part B -------------------
def groupBadge(lines) -> int:
    # Variables for score and calculations
    points = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    group = []
    # Iterate through all words
    for i in lines:
        group.append(i)
        # When the group is three, we will begin looking for common character
        if len(group) == 3:
            # Taking one of the words for refference
            word = group[0]
            # Iterate through every character in the word
            for character in word:
                # Compare if the other words have it
                # Ideally we wound want to filter out already searched
                # Characters 
                if character in group[1] and character in group[2]:
                    # Adding score and reset group
                    score += points.index(character) + 1
                    group.clear()

                    break 
    return score



def main():
    with open('./Day3/input.txt') as f:
            
            # Every row into array
            lines = f.readlines()
            # First part
            sumOfdups = sumOfDups(lines)
            groupBadgeSum = groupBadge(lines)

            print(f"Answer in part A: {sumOfdups} \nAnswer for part B: {groupBadgeSum}")
            

main()