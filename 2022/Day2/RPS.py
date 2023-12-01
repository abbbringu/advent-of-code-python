
# ------------------- Part A -------------------
def personalTotalScore(lines: list) -> int:
    rps = ['A', 'B', 'C']
    rpsme = ['X\n', 'Y\n', 'Z\n']
    score = 0
    for i in lines:
        # Splitting each value into 
        values = i.split(" ")

        # Looking att difference in index that is ordered Rock, Paper, Scissors
        # And the distance between these will decide the winner with opponents score first
        difference = (rps.index(values[0]) - rpsme.index(values[1])) % 3

        # If we have same index, then we have the same value (Draw)
        if difference == 0:
            score += 3

        # Win cases, if the difference is 2
        elif difference == 2:
            score += 6
        
        # The rest of the cases will be lost, so we will not add additional scores 
        # So we add the points for the rps we choose

        score += (rpsme.index(values[1]) + 1) 

    return score


# ------------------- Part B -------------------
def personalTotalScoreNew(lines: list) -> int:
    rps = ['A', 'B', 'C']
    winCondition = ['X\n', 'Y\n', 'Z\n']
    # Total Score
    score = 0
    ourHand = 0
    
    for i in lines:
        # Splitting each value into 
        values = i.split(" ")

        otherPlayer = rps.index(values[0]) 
        winIndex = winCondition.index(values[1])
        
        # Lose condition
        if winIndex == 0:
            # Decide our hand
            ourHand = (otherPlayer - 1) % 3
        # Draw
        elif winIndex == 1:
            ourHand = otherPlayer
        # Win
        elif winIndex == 2:
            ourHand = (otherPlayer + 1) % 3 

        # Score added is combination of match outcome and hand
        score += (ourHand + 1) + winIndex * 3

    return score

def main():
    with open('./Day2/input.txt') as f:
            # Every row into array
            lines = f.readlines()
            # First part
            total = personalTotalScore(lines)
            # Second part
            totalNewScore = personalTotalScoreNew(lines)
            # Printing both of them
            print(f"Total score: {total} \nNew score is {totalNewScore}")
            

main()