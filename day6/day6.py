import sys
sys.setrecursionlimit(20000)

def findFirstFourRepeatedChars(inputString, trailer, index, numbersInSet):
    if len(set(inputString[trailer:index])) == numbersInSet:
        return index
    else: 
        return findFirstFourRepeatedChars(inputString, trailer + 1, index + 1, numbersInSet)


with open('./input.txt') as f:
    raw = f.read()
    numbersInSetTask1 = 4
    numbersInSetTask2 = 14
    resultTask1 = findFirstFourRepeatedChars(raw, 0, numbersInSetTask1, numbersInSetTask1)
    resultTask2 = findFirstFourRepeatedChars(raw, 0, numbersInSetTask2, numbersInSetTask2)
    print(
    """
    Result task 1: {}
    Result task 2: {}
    """.format(resultTask1, resultTask2)) 
