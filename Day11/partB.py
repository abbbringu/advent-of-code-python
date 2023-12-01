class monkey:
    # Variables
    holding = []
    operation = ""
    operationBy = ""
    testDiv = 0
    throwTrue = 0
    throwFalse = 0

    def addHolding(self, toAdd):
        #print(self.holding)
        self.holding.append(toAdd)
        #print(self.holding)

    def testCondition(self, value):
        # Testing if worry is matching condition
        return 0 == value % int(self.testDiv)

    def inspect(self):
        # Different operation for inspection
        if self.operation == "+":
            self.holding[0] += int(self.operationBy)
        elif self.operation == "*":
            if self.operationBy == "old\n":
                self.holding[0] = pow(self.holding[0], 2)
            else:
                self.holding[0] *= int(self.operationBy)
        # Getting bored, divide by 3

        


# ------------------- Part B -------------------
def mostActivity(lines, rounds = 20):
    inspectCount = [0 for i in range(8)]
    monkeys = []
    attribute = []
    mod = 1
    # Building the monkeys array
    for row in lines:
        if row == '\n':
            continue
        row = row.lstrip()
        row = row.split(" ")
        attribute.append(row)
    for index in range(8):
        monkeys.append(monkey())
        # Getting each attribute for the monkey
        monkeyindex = index * 6        # The addition is the line of the current monkey
        monkeys[-1].holding    = [int(i[:-1])for i in attribute[monkeyindex + 1][2:]]
        monkeys[-1].operationBy = attribute[monkeyindex + 2][-1]
        monkeys[-1].operation   = attribute[monkeyindex + 2][-2]
        monkeys[-1].testDiv     = int(attribute[monkeyindex + 3][-1])
        monkeys[-1].throwTrue   = int(attribute[monkeyindex + 4][-1])
        monkeys[-1].throwFalse  = int(attribute[monkeyindex + 5][-1])
        mod *= monkeys[-1].testDiv # Getting all test divs into mod
    # Acting out the rounds
    for _ in range(rounds):
        # Every monkey have an action in their order
        for index in range(len(monkeys)):
            #times = len(monkeys[index].holding)
            # Inspecting amount of item their holding
            while monkeys[index].holding:
                # Inspect and add to count
                monkeys[index].inspect()
                inspectCount[index] += 1
                # Test the condition to see who to throw
                toAdd = monkeys[index].holding.pop(0)
                toAdd %= mod # To limit the size, and optimization
                newIndex = monkeys[index]
                if monkeys[index].testCondition(toAdd):
                    monkeys[newIndex.throwTrue].addHolding(toAdd)
                else:
                    monkeys[newIndex.throwFalse].addHolding(toAdd)

    largest = max(inspectCount)
    inspectCount.remove(largest)
    return largest * max(inspectCount)











def main():
    with open('./Day11/input.txt') as f:
        # Every row into array
        lines = f.readlines()
        # Part A
        # Part B
        print("Part B:", mostActivity(lines, rounds=10000))
        #print(drawing(lines))

main()