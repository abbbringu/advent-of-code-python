import re


def countValidGames(lines):
    # Valid game with 12 red cubes, 13 green cubes, and 14 blue cubes.
    vaildTest = [12,13,14]
    validGame = 0
    for game in lines:
        validFlag = True
        game = game.split(":")
        gameId = game[0]
        sets = game[1].strip().split(";")
        for set in sets:
            set = set.split(",")
            # print(set)
            for round in set:
                color = 2
                if "red" in round:
                    color = 0
                elif "green" in round:
                    color = 1
                round = re.sub('\D','',round)
                if int(round) > vaildTest[color]: validFlag = False
        validGame += int(re.sub('\D','',gameId))*validFlag
    print("The sum of game ID which are valid:",validGame)



def minimumCubes(lines):
    # Valid game with 12 red cubes, 13 green cubes, and 14 blue cubes.
    totalSum = 0
    for game in lines:
        # RGB
        colors = [0,0,0]
        game = game.split(":")
        sets = game[1].strip().split(";")
        for set in sets:
            set = set.split(",")
            for round in set:
                color = 2
                if "red" in round:
                    color = 0
                elif "green" in round:
                    color = 1
                round = re.sub('\D','',round)
                colors[color] = max(int(round), colors[color])
        totalSum += colors[0]*colors[1]*colors[2]
    print("Sum of power of each game:",totalSum)



def main():
    # Access the file
    with open('./2023/Day2/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        countValidGames(lines)
        minimumCubes(lines)
main()
