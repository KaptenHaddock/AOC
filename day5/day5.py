import re
containerRegex = r"[A-Z]"
definitionRow = r"[0-9]{1,2}"
containers = {}
containerChars = []

def readInstructions(arr, crateMoverVersion):
    for line in arr:
        foundInstructions = re.findall(definitionRow, line)
        fromContainerNumber = int(foundInstructions[1])
        toContainerNumber = int(foundInstructions[2])
        noOfContainers = int(foundInstructions[0])
        
        # create mover 9001
        if crateMoverVersion == 9001:
            moving = containers[fromContainerNumber][:noOfContainers]
            containers[toContainerNumber] = moving + containers[toContainerNumber]
            del containers[fromContainerNumber][:noOfContainers]
            print(
                """
                CrateMover 9001
                moved {}
                from container {}
                to container {}
                """.format(moving, fromContainerNumber, toContainerNumber))
        
        # create mover 9000
        else:
            for i in range(0, noOfContainers):
                moving = containers[fromContainerNumber][0]
                containers[toContainerNumber].insert(0,moving)
                del containers[fromContainerNumber][0]
                print(
                """
                CrateMover 9000
                moved {}
                from container {}
                to container {}
                """.format(moving, fromContainerNumber, toContainerNumber))
    

containerNo = 0
crateMoverVersion = 9001 # 9000 or 9001
with open('./input.txt') as f:
    raw = f.read()
    for index, char in enumerate(raw):
        # marks start of instructions
        if char == 'm':
            craneInstructions = raw[index:].split('\n')
            readInstructions(craneInstructions, crateMoverVersion)
            break
        if char == '\n':
            containerNo = 0
            continue
        foundContainerContent = re.findall(containerRegex, char)
        if foundContainerContent:
            if containerNo not in containers:
                # Allocate new container
                containers[containerNo] = []
            containers[containerNo].append(foundContainerContent[0])
        if index % 4 == 0:
            containerNo += 1
            containerChars.append(char)

resultstring = ""       
for i in range(1, len(containers) +1 ):
    print(
    """
    Top in container {} was {}
    """.format(i, containers[i][0][0]))
    resultstring += containers[i][0][0]

print(
"""
Result string is "{}"
""".format(resultstring))