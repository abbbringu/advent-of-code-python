
"""
We need to check which instruction is played
and then add the to current before anything and then check
if we should calculate the signal strength
This is to emulate that we are checking during cycle
And the last thing is to update x with the relevant value.

"""
# ------------------- Part A -------------------
def cycle(lines):
    current = 0
    regx = 1
    sumOfSignalStrength = 0
    checkpoints = [i for i in range(20, 221, 40)]
    for row in lines:
        # If row is noop (no operation)
        if row == 'noop\n' or row == 'noop':
            # See during the cycle, if it's within checkpoints 
            current += 1
            if current in checkpoints:
                sumOfSignalStrength += regx * current   
        else:
            # The 2 cycles for addition
            for _ in range(2):
                current += 1
                if current in checkpoints:
                    sumOfSignalStrength += regx * current
                    
            # Splitting and preparing variables
            instruc = row.split(" ")
            instruc[1] = int(instruc[1])
            # Updating register x
            regx += instruc[1]

    return sumOfSignalStrength


# ------------------- Part B -------------------
def drawing(lines):
    current = 0
    regx = 1
    display = ""
    # Note that the chekcpoints are different from part A
    checkpoints = [i for i in range(40, 241, 40)]
    for row in lines:
        # If row is noop (no operation)
        if row == 'noop\n' or row == 'noop':
            # Look what character to add
            current += 1
            # If within the lit pixel position
            if abs(regx - (current - 1)) < 2:
                display += "#"
            else:
                display += "."
            # New line
            if current in checkpoints:
                display += '\n'  
                current = 0
        else:
            # The 2 cycles for addition
            for _ in range(2):
                current += 1
                # Within lit pixel
                if abs(regx - (current - 1)) < 2:
                    display += "#"
                else:
                    display += "." 
                # Newline
                if current in checkpoints:
                    display += '\n'
                    current = 0
            # Splitting and preparing variables
            instruc = row.split(" ")
            instruc[1] = int(instruc[1])
            # Updating register x
            regx += instruc[1]

    return display

 





def main():
    with open('./Day10/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        print("Part A:", cycle(lines))
        # Part B
        print(drawing(lines))
main()