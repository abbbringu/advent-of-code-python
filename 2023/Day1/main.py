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
        my_string = "one two three four five six seven eight nine"
        my_pattern = "(?=(one|two|three|four|five|six|seven|eight|nine))"
        matches = [match.group(0)
                   for match in re.finditer(my_pattern, my_string)]
        print(matches)

        test = [match for match in re.finditer(my_pattern, line)]
        print(test)
        matches = re.finditer(
            "one|two|three|four|five|six|seven|eight|nine", line)
        m = re.finditer(r"\d", line)

        for match in m:
            numerical.append((int(match.group()), match.start()))
        for match in matches:
            print(match.group())
            numerical.append(
                (numberList.index(match.group()), match.start()))

        numerical.sort(key=lambda x: x[1])
        hi, lo = numerical[0][0], numerical[-1][0]

        comb = str(hi) + str(lo)
        print(comb, line, numerical)
        sumOfCalibrations += int(comb)
    print(sumOfCalibrations)


def main():
    # Access the file
    with open('./2023/Day1/input.txt') as f:
        # Every row into array
        lines = f.readlines()

        # jkrbkfsevencnvzp89vhmsdcfcthreetwonedrl
        partTwo(["eightwo"])

        # 55358 är svaret till ryans
main()
