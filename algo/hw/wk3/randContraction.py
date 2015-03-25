#!/usr/bin/env python

from collections import defaultdict 
from math import log
from copy import deepcopy
import random

# seems slow; should profile

def main():
    (vertices,edges) = readInput("kargerMinCut.txt")
    N = len(vertices)
    minCut = 99999 #cheater
#     for i in range(0,int(N*N*log(N))+1):
    for i in range(0,100):
        thisMinCut = randomContraction(deepcopy(vertices),deepcopy(edges))
        if thisMinCut < minCut:
            minCut = thisMinCut
    print
    print minCut


def readInput(fn):
    f = open(fn)
    vertices = defaultdict(list)
    nEdges = 0
    edges = {}
    for line in f.readlines():
        lineNumbers = [ int(x) for x in line.split() ]
        
        iU = lineNumbers[0]
        for n in lineNumbers[1:]:
            iV = n
            # we've already seen the combination and added
            # it if nVertex <= thisVertex
            if iV > iU:
                vertices[iU].append(nEdges)
                vertices[iV].append(nEdges)
                edges[nEdges] = [iU,iV] if iU < iV else [iV,iU]
                nEdges += 1

    return (vertices,edges)


def randomContraction(vertices,edges):

    random.seed()
     
    while len(vertices) > 2:
        # pick a remaining edge at random
        edgeToPop = random.choice(edges.keys())

        (iU,iV) = edges.pop(edgeToPop)
        vertices[iU].remove(edgeToPop)
        vertices[iV].remove(edgeToPop)
        for edge in vertices[iV]:
            
            # find the right vertex to replace
            if edges[edge][0] == iV:
                edges[edge][0] = iU
            elif edges[edge][1] == iV:
                edges[edge][1] = iU
            else:
                print "this should never friggin happen"

            # only add it if it's not a self loop
            # and if it is, remove it from list and from
            # other side of the edge (i.e. iU)
            if edges[edge][0] != edges[edge][1]:
                vertices[iU].append(edge)
            else:
                edges.pop(edge)
                vertices[iU].remove(edge)

        vertices.pop(iV)

    return len(edges)

if __name__ == "__main__":
    main()
