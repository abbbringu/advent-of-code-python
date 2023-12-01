
# ------------------- Part A -------------------
def containEachOther(lines) -> int:
    amountOfFullContain = 0
    # Split pairs into array
    for pairs in lines:

        # Split group to worker
        PairRange = pairs.split(",")
        # Split each worker time range ex ["2", "5"]
        Range1, Range2 = PairRange[0].split("-"), PairRange[1].split("-")
        
        # Take the difference
        firstTime = int(Range1[0]) - int(Range2[0])
        secondTime = int(Range2[1]) - int(Range1[1]) # Notice Range2 comes first here

        """
        Three cases:
        ...45678..      First and second will be negative
        ....567...      (Range1 domineering)

        ...45678..      First and second will be positive
        ..3456789.      (Range2 domineering)

        ...45678..      One of them will be 0, thus automatically
        ...45678..      means on contain the other
        """

        # Match all three cases with this multiplication and comparison
        if firstTime * secondTime >= 0:
            amountOfFullContain += 1

    return amountOfFullContain


# ------------------- Part B -------------------
def overlap(lines) -> int:
    amountOverlap = 0

    for pairs in lines:

        # Split group to worker
        PairRange = pairs.split(",")
        # Split each worker time range ex ["2", "5"]
        Range1, Range2 = PairRange[0].split("-"), PairRange[1].split("-")
        
        # Take the difference
        firstTime = int(Range1[0]) - int(Range2[1]) # Notice it's not the same as in part A
        secondTime = int(Range1[1]) - int(Range2[0]) 

        """
        Two cases:
        ...45678..      first will be negative and second will be positive
        ....56789.      first = 4 - 9       second = 8 - 5

        ...45678..      first = 4 - 7       second = 8 - 3
        ..34567...      

        If one range does not overlap, first and second will both be either
        negative or positive

        The product will be negative if they overlap, the one range is the the right or left
        they both will either be positive or negative, meaning their product would be > 0
        And if difference is 0, it will also overlap ("They have the same value")
        """

        if firstTime * secondTime <= 0:
            amountOverlap += 1

    return amountOverlap






def main():
    with open('./Day4/input.txt') as f:
            # Every row into array
            lines = f.readlines()
            # Part A
            fullContain = containEachOther(lines)
            # Part B
            overlapping = overlap(lines)
            print(f"Answer in part A: {fullContain} \nAnswer for part B: {overlapping}")

main()