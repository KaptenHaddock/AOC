from statistics import median

total = 0
groupTotal = 0
groupCounter = []

def getVal(char):
    value = ord(char) - 96
    if char.isupper():
        value = ord(char) - 38
    return value

with open('./input.txt') as f:
    for line in f.readlines():
        line = line.strip()
        groupCounter.append(line)
            
        foundMedian = int(median([0, len(line)]))
        firstCompartment = line[:foundMedian]
        secondCompartment = line[foundMedian:]

        # Task 1
        for char in firstCompartment:
            if char in secondCompartment:
                value = getVal(char)
                print('Found char present in both compartments', char, "value is ", value)
                total += value
                break
        
        # Task 2
        if len(groupCounter) % 3  == 0:
            for char in groupCounter[0]:
                if char in groupCounter[1] and char in groupCounter[2]:
                    print('Found group char', char, "value is ", value)
                    groupTotal += getVal(char)
                    break
            groupCounter = []
print(total, groupTotal)


