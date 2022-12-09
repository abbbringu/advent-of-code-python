
# ------------------- Part A & B -------------------

def findMark(word, inc = 1):
    index = 0
    while True:

        # Take the inc chars and copy them to code
        code = word[index : index + inc]
        found = True
        
        # Check that it doesn't run out of elements
        if(len(code) < inc):
            return -1

        # if there are no dups in 3 of them, we can pass
        for letter in code:
            if(code.count(letter) != 1):                # Comparing every letter
                index += code.index(letter) + 1         # Instead of inc with 1, we ince with the index of letter + 1
                found = False                           # Setting variable to not return
                break

        if(found): return (index + inc)                 # If no dups, then return
        

def main():
    with open('./Day6/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        word = lines[0]
        # Part A
        print(f"Part A: {findMark(word, 4)}")
        # Part B
        print(f"Part B: {findMark(word, 14)}")


main()