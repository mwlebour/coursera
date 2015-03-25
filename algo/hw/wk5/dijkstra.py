#!/usr/bin/env python

# from __future__ import print_function
from collections import defaultdict 
import sys

# def outerLoop(vertices,edges):
#     s = 1
#     for t in [7,37,59,82,99,115,133,165,188,197]:
#         l = dijkstra(vertices,edges,s,t) 
#         print(l if l != -1 else 1000000,end=',')
# 
#     print()

# def dijkstra(vertices,edges,s,t):
def dijkstra(vertices,edges):

    # starting with s = 1
    s = 1

    # X = {S} # vertices processed so far
    x = {}
    x[s] = 1
    # NX maintain to be V-X
    nx = dict.fromkeys(vertices.keys(),1)
    del nx[s]
    # A[S] = 0 # computed shortest path distances
    a = {}
    a[s] = 0

    # B[S] = empty path # computed shortest path
    # b = defaultdict(list)
    # b[s] = []

    # this probably isn't quite correct, but whatevs
    while len(x) != len(vertices):
#         print x,nx
#         print len(x),len(nx)

        # dijkstrizable edge tracking
        minEdge = None
        minLength = None
        # slow ass loop over all edges 
        for edge,(source,sink,length) in edges.iteritems():
            # could theoretically check if both are on 
            # the left

            # check: is sink on the left and source 
            # on the right or vice versa or whatever
            # you get it
            if source in x and sink in nx:
                #BOOM, candidate for dijkstrizing
                if minLength == None or a[source] + length < minLength:
                    minLength = a[source] + length
                    minEdge = edge

            if sink in x and source in nx:
                #BOOM, candidate for dijkstrizing
                if minLength == None or a[sink] + length < minLength:
                    minLength = a[sink] + length
                    minEdge = edge
            
        # made it out of loop over edges
        if minEdge == None:
            # rest of the vertices aren't connected
            break
        (source,sink,length) = edges[minEdge]
        if sink in x:
            if source in x:
                print("WTF:",source,sink,length)
            a[source] = a[sink] + length
            del nx[source]
            x[source] = 1
        elif source in x:
            if sink in x:
                print("WTF:",source,sink,length)
            a[sink] = a[source] + length
            del nx[sink]
            x[sink] = 1
        else: 
            print("this should never happen")

    # while X != V:  
    #   for each v,w where v in X and w not in X
    #   pick edge that minimizes A[v] + l_vw
    #   add w to X
    #   set A[w] = A[v] + l_vw
    return a


def readInput(fn):
    vertices = defaultdict(dict)
    nEdges = 0
    edges = {}
    f = open(fn)
    for line in f:
        items = [ x.strip() for x in line.split() ]
        source = int(items[0])
        for x in items[1:]:
            y = x.split(',')
            (sink,length) = int(y[0]),int(y[1])
            vertices[source][nEdges] = 1
            vertices[sink][nEdges] = 1
            edges[nEdges] = (source,sink,length) if source < sink else (sink,source,length)
            nEdges += 1

    f.close()

#         f = open(pklFn,"w")
#         pickle.dump( (vertices,edges) , f )
#         f.close()
    return (vertices,edges)

if __name__ == "__main__":
    fn = "ex1.txt" if len(sys.argv) != 2 else sys.argv[1]
    (vertices,edges) = readInput(fn)
#     outerLoop(vertices,edges)
    s = dijkstra(vertices,edges)
    for t in [1,7,37,59,82,99,115,133,165,188,197]:
        print s[t]
