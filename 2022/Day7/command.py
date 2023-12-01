


""" 
We want to take all files which is under 100.000 size and add them together
We don't consider that we will count certain files 2 times and we will need to 
add all files to see if there are bigger than the set amount. 

Here are our assuptions:
1. If a dir within another dir is over 100.000, the the parents will not be added
2. the size of the dir is the files within the dir, and it's children. 
3. The children should be threated as the parents counting them in too.
4. The input don't have / more than once at the beginning

don't know if we can do it recurcivly, or not... We need to somehow keep track of the dir
while we deep deeper within the dir. 

What if we have an array like current directory with tuples of the name and size. 
We treat it like a stack and for each we pop, we add to the value it's parent..... 
This might work....

Everytime we do a cd, we add the value to the stack. 
we go through every file and add it to the tupel 

"""
def addDirs(lines):
    # Hosting all the data for our system
    size = 0
    toAdd = 0
    data = []

    for row in lines:
        if(row == "\n"):
            return size
        # Splitting the row into a list divided by spaces
        row = row.split(" ")
        # We first ceck if the line is a command
        if row[0] == '$':
            # Need to check which command
            if row[1] == "cd":
                if row[2] == "..":
                    """
                    Check if we should add (size is less than 100.000)
                    either way we should add it to it's parent.
                    """
                    if data[0][1] < 100_000:
                        size += data[0][1]
                    addToPrev = data.pop()    # Deepest
                    data[0][1] += addToPrev[1]
                else:
                    data.push((row[2], 0))
            elif row[1] == "ls":
                print("ls")
        else:
            if row[0] != "dir":
                data[0][1] += int(row[0])
                # Add dir to current dir














def main(): 
    with open('./Day7/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        addDirs(lines)



main()