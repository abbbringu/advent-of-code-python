
# ------------------- Part A -------------------
def visibleTrees(lines):
    visible = 0
    # Building forest
    # Most cases with -1 is to consider \n at the end
    for row in range(len(lines)):
        # If either top or bottom row, it's visible by default
        if row == 0 or row == len(lines) -1:
            visible += len(lines[0]) - 1
            continue
        
        # Loop through each tree in a row
        for tree in range(len(lines[row]) - 1):
            isVisible = False    
            # If at the edge add to visible
            if tree == 0 or tree == len(lines[0]) - 2:
                visible += 1
                continue
            # Setting variables for clarity
            x = tree
            y = row
            position = 1


            # Check left from curret position
            while x - position > -1:
                isVisible = True  
                #If any tree cover the current
                if lines[y][x] <= lines[y][x-position]:
                    isVisible = False
                    break
                position += 1

            # if not covered, than add to visible and 
            # Continue
            if isVisible:
                visible += 1
                continue
            
            position = 1
            # Check to the right
            while x + position < len(lines[0]) -1:
                isVisible = True 
                if lines[y][x] <= lines[y][x+position]:
                    isVisible = False
                    break
                position += 1
            
            if isVisible:
                visible += 1
                continue
            
            position = 1
            # Check above
            while y - position > -1:
                isVisible = True 
                if lines[y][x] <= lines[y-position][x]:
                    isVisible = False
                    break
                position += 1
            
            if isVisible:
                visible += 1
                continue
            
            position = 1
            # Check below
            while y+position < len(lines):
                isVisible = True
                if lines[y][x] <= lines[y + position][x]:
                    isVisible = False
                    break
                position += 1
            
            if isVisible:
                visible += 1


    return(visible)


# ------------------- Part B -------------------
def scenicPoints(lines):
    mostPoint = 0
    for row in range(len(lines) - 1):

        if row == 0 or row == len(lines) -1:
            continue
        for tree in range(len(lines[row]) - 1):
            if tree == 0 or tree == len(lines[0]) - 2:
                continue
            x = tree
            y = row
            value = lines[y][x]
            left,right,up,down = 0,0,0,0
            position = 1


            # Check left from curret position
            while x - position > -1:
                #If any tree cover the current
                if lines[y][x] <= lines[y][x-position]:
                    left += 1
                    break
                position += 1
                left += 1
            
            position = 1
            # Check to the right
            while x + position < len(lines[0]) -1:
                if lines[y][x] <= lines[y][x+position]:
                    right += 1
                    break
                position += 1
                right += 1
            
            position = 1
            # Check above
            while y - position > -1:
                if lines[y][x] <= lines[y-position][x]:
                    up += 1
                    break
                position += 1
                up += 1
            
            position = 1
            # Check below
            while y+position < len(lines):
                if lines[y][x] <= lines[y + position][x]:
                    down += 1
                    break
                position += 1
                down += 1
           #print((up*down*left*right))
            mostPoint = max(mostPoint, (up*down*left*right))
        
    return mostPoint


def main():
    with open('./Day8/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        print(visibleTrees(lines))
        # Part B
        print(scenicPoints(lines))



main()