
import numpy as np

totalOverlaps = 0
totalIntersections = 0

def createAreaVector(instruction):
        areaStartAndStop = instruction.split('-')
        areaStart = int(areaStartAndStop[0])
        areaStop = int(areaStartAndStop[1])
        areaSize = (areaStop - areaStart) + 1
        return np.linspace(areaStart, areaStop, areaSize)

with open('./input.txt') as f:
    rawRows = f.readlines()
    for row in rawRows:
        areasOnRow = row.strip().split(',')
        area1vector = createAreaVector(areasOnRow[0])
        area2vector = createAreaVector(areasOnRow[1])
        # vector contains which vector element(s)?
        intersectingElements = np.intersect1d(area1vector, area2vector, assume_unique=False)
        # Any overlap?
        if len(intersectingElements) > 0:
            totalIntersections += 1
        # Total overlap of vector elements
        if len(intersectingElements) == len(area1vector) or len(intersectingElements) == len(area2vector):
            totalOverlaps += 1

print(
"""
Areas with 100% overlap' -> {totalOverlaps}
Areas with any overlap' -> {totalIntersections}
"""
.format(totalOverlaps=totalOverlaps, totalIntersections=totalIntersections))