#!/usr/bin/env python

from collections import defaultdict 
from math import log
from copy import deepcopy
import random

class Vertex:
    """Has a unique identifier and a list of edges"""
    unique = 10000
    def __init__(self,identity=-1):
        if identity == -1:
            self.identity = Vertex.unique
            Vertex.unique += 1
        else: 
            self.identity = identity
        self.edges = {}

    def addEdge(self,e):
        self.edges[e] = 1

    def __getitem__(self,key):
        return self.edges[e]

    def __setitem__(self,key,value):
        self.edges[key] = value

    def __str__(self):
        return str(self.identity)

    def __hash__(self):
        return self.identity

    def __eq__(self,other):
        return self.identity == other.identity

    def __gt__(self,other):
        return self.identity > other.identity

    def __lt__(self,other):
        return self.identity < other.identity

    def __ge__(self,other):
        return self.identity >= other.identity

    def __le__(self,other):
        return self.identity <= other.identity


class Edge:
    """Has a unique identifier and a pair of vertices"""
    unique = 10000
    def __init__(self,u,v):
        self.identity = Edge.unique
        Edge.unique += 1
        (self.u,self.v) = (u,v) if u < v else (v,u)

    def vertices(self):
        return (self.u,self.v)

    def __str__(self):
        return "(" + str(self.u) + "," + str(self.v) + ")"

#     def __eq__(self,other):
#         if isinstance(other,Edge):
#             return other.identity == self.identity
#         else:
#             return NotImplemented


def main():
    (vertices,edges) = readInput("kargerMinCut.txt")
    N = len(vertices)
    for edge in edges:
        print edge
#     minCut = 99999 #cheater
#     for i in range(0,int(N*N*log(N))+1):
#         thisMinCut = randomContraction(deepcopy(vertices),deepcopy(edges))
#         print thisMinCut
#         if thisMinCut < minCut:
#             minCut = thisMinCut
#     print minCut


def readInput(fn):
    f = open(fn)
    vertices = {}
    edges = {}
    for line in f.readlines():
        lineNumbers = [ int(x) for x in line.split() ]
        
        thisVertex = Vertex(lineNumbers[0])
        vertices[thisVertex] = 1
        for n in lineNumbers[1:]:
            # note that the hash value for a vertex
            # is just its identifier, so new 
            # instances of Vertex will hash to 
            # the same value
            nVertex = Vertex(n)
            # we've already seen the combination and added
            # it if nVertex <= thisVertex
            if nVertex > thisVertex:
                vertices[nVertex] = 1
                thisEdge = Edge(thisVertex,nVertex)
                edges[thisEdge] = 1
                thisVertex.addEdge(thisEdge)
                nVertex.addEdge(thisEdge)

    return (vertices,edges)


def randomContraction(vertices,edges):

    random.seed()
     
    while len(vertices) > 2:
        # pick a remaining edge at random
        toPop = random.choice(edges.keys())

        edges.pop(toPop)
        vertices[toPop[0]].pop(toPop)
        vertices[toPop[1]].pop(toPop)

        edgesToCheck = vertices.pop(toPop[1])
        for edge in edgesToCheck.keys():
            if edge[0] == toPop[1]:
                newEdge = (toPop[0],edge[1]) if toPop[0] < edge[1] else (edge[1],toPop[0])
                vertices[edge[1]].pop(edge)
            elif edge[1] == toPop[1]:
                newEdge = (toPop[0],edge[0]) if toPop[0] < edge[0] else (edge[0],toPop[0])
                vertices[edge[0]].pop(edge)
            else:
                print "this should never friggin happen"

            # remove old edge and add updated edge
            # print toPop,edge,newEdge
            edges.pop(edge)
            if newEdge[0] != newEdge[1]:
                edges[newEdge] = 1
                vertices[newEdge[0]][newEdge] = 1
                vertices[newEdge[1]][newEdge] = 1



    return len(edges)

if __name__ == "__main__":
    main()
