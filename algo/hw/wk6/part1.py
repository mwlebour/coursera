#!/usr/bin/env python

from collections import defaultdict 
from bisect import bisect_left,bisect_right
import sys

def readInput(fn):
    myHash = {}
    myArray = []
    f = open(fn)
    for line in f:
        i = int(line.strip())
        if i not in myHash:
            myArray.append(i)
#         else:
#             print i

        myHash[i] = True
    f.close()

    return (myHash,myArray)

if __name__ == "__main__":
    fn = "ints.txt" if len(sys.argv) != 2 else sys.argv[1]
    (myHash,myArray) = readInput(fn)

    myArray.sort()
    length = len(myArray)
    count = 0
    sumValues = {}
    for i,v in enumerate(myArray):
        l = bisect_left(myArray,-10000 - v)
        g = bisect_right(myArray,10000 - v)
#         print v
#         print "v,i,l,a[l],v+a[g],g,a[g],v+a[g]: %d,%d,%d,%d,%d,%d,%d,%d" % (v,i,l,myArray[l],v+myArray[l],g,myArray[g],v+myArray[g])

        for j in range(max(i+1,l-3),min(length,g+3)):
            if v == myArray[j]: continue
            if v+myArray[j] >= -10000 and v+myArray[j] <= 10000:
#                 print v,myArray[j],v+myArray[j]
                sumValues[v+myArray[j]] = True
    print len(sumValues)


