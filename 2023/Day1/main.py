import re


def partOne(lines):
    sumOfCalibrations = 0
    for line in lines:
        # Find the int in the string and combine them convert them to int to add to the sum
        m = re.findall(r"\d", line)
        combStr = m[0] + m[-1]
        sumOfCalibrations += int(combStr)

    print("The sum of the calibrations are:", sumOfCalibrations)


def partTwo(lines):
    sumOfCalibrations = 0
    numberList = ["zero", "one", "two", "three", "four",
                  "five", "six", "seven", "eight", "nine"]
    for line in lines:
        numerical = []
        # Search for each letter digit at a time, since finditer doesn't consider overlap
        for number in numberList:
            [numerical.append((numberList.index(match.group()), match.start())) for match in re.finditer(number, line)]
        m = re.finditer(r"\d", line)

        # Match with digits and append to array.
        for match in m:
            numerical.append((int(match.group()), match.start()))

        # Sort them accourding to their position
        numerical.sort(key=lambda x: x[1])
        # Get the two with the highest and lowest position in the string
        hi, lo = numerical[0][0], numerical[-1][0]

        comb = str(hi) + str(lo)
        # print(comb, line, numerical)
        sumOfCalibrations += int(comb)

    print("Consdier letter digits, the correct calibrations are:", sumOfCalibrations)


def main():
    # Access the file
    with open('./2023/Day1/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        partTwo(lines)

        # 55358 är svaret till ryans
main()
