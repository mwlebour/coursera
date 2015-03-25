#!/usr/bin/env python

from collections import defaultdict 
from math import log
from copy import deepcopy
from time import sleep
import sys, os.path, pickle, random, operator, logging

logging.basicConfig(
    format="%(asctime)s: %(levelname)s: %(message)s", 
    level=logging.INFO, 
    datefmt='%Y/%m/%d %H:%M:%S'
)
# logger = logging.getLogger('kosaraju')
# logger.setLevel(logging.DEBUG)
# formatter = logging.Formatter(
#     "%(asctime)s %(levelname)s: %(message)s", 
#     datefmt='%Y/%m/%d %H:%M:%S'
# )
# fh = logging.FileHandler("kosaraju.out")
# fh.setLevel(logging.DEBUG)
# fh.setFormatter(formatter)
# ch = logging.StreamHandler()
# ch.setLevel(logging.ERROR)
# ch.setFormatter(formatter)
# logger.addHandler(fh)
# logger.addHandler(ch)

logging.info("kosaraju is loading, welcome")

def kosaraju(vertices,edges):
    logging.info(
        'kosaraju: starting algorithm with nVertices = %d and nEdges = %d' 
        % ( len(vertices),len(edges) ) 
    )

    logging.debug('entering first dfsLoop pass None as f')
    f = dfsLoop(vertices,edges,None)
    logging.debug(
        'kosaraju: out of first dfsLoop, len(f) = %d, f[1] = %d' 
        % (len(f),f[1])
    )

    logging.debug('entering second dfsLoop passing newly found f')
    leaders = dfsLoop(vertices,edges,f)
    logging.debug(
        'kosaraju: out of second dfsLoop, len(leaders) = %d, leaders[1] = %d'
        % (len(leaders), leaders[1])
    )

    logging.debug('kosaraju: counting the number of vertices per leader')
    counts = defaultdict(int)
    for vertex,leader in leaders.iteritems():
        counts[leader] += 1
    winners = sorted(counts.iteritems(), key=operator.itemgetter(1),reverse=True)
    logging.info("kosaraju: found %d SSCs, here's the top five" % len(winners))
    for i,(leader,count) in enumerate(winners[0:5]):
        logging.info("SSC #%d: %d" % (i+1,count))

    logging.info('kosaraju: SSCs supposedly successfully sought, sayonara.')
    return winners[0:5]


def dfsLoop(vertices,edges,f):
    # let's do some work son
    # if f is null, then we need to compute the finishing times
    # if f is non-null, then assume it has the finishing times
    # encoded in it such that:
    # f[i] = n, the ith finishing time is vertex n
    # or n finished in ith place
    # this way you can traverse f backwards to get the next element

    t = 0    # to keep track of finishing time
    s = None # 
    useF = True
    explored = {}
    leader = {}
    if f == None:
        logging.debug(
            'dfsLoop: f is None, not using f this pass, length of f is %d' 
            % (len(vertices) + 1)
        )
        useF = False
        f = (len(vertices) + 1) * [None]
    else:
        logging.debug('dfsLoop: f is full, will use f to decide where to start')

    logging.debug('dfsLoop: entering loop over unexplored vertices')
    # big assumption: # of vertices == max vertex number
    for i in range(len(vertices),0,-1):
        logging.debug( "%d %d %d" % (i,len(f),len(vertices)) )
        iU = i if not useF else f[i]
        logging.debug('dfsLoop: processing vertex number %d' % i)
        if useF:
            logging.debug('dfsLoop: but, useF is True so vertex number is actually %d' % iU)
        if iU not in explored:
            logging.debug('dfsLoop: woop, found one, %d is unexplored' % iU)
            logging.debug('dfsLoop: setting leader s, to %d' % iU)
            s = iU
            logging.debug('dfsLoop: entering dfs()')
            # recursion version:
            # t = dfs(vertices,edges,iU,explored,leader,useF,f,s,t)
            # stack version:
            t = dfs2(vertices,edges,iU,explored,leader,useF,f,s,t)
        else:
            logging.debug('dfsLoop: vertex %d already explored. nothing to see here, move along' % iU)


    if useF:
        return leader
    else:
        return f

def dfs(vertices,edges,iU,explored,leader,useF,f,s,t):
    logging.debug(
        "dfs: marking %d as explored and setting it's leader to %d" 
        % (iU,s)
    )
    explored[iU] = 1
    leader[iU] = s

    logging.debug(
        "dfs: using source as %s and sink as %s because useF is %s" 
        % (("source","sink","TRUE") if useF else ("sink","source","TRUE"))
    )
    (source,sink) = (0,1) if useF else (1,0)
    
    logging.debug(
        "dfs: staring loop over %d edges for vertex %d" 
        % ( len(vertices[iU]), iU )
    )
    for edge in vertices[iU]:
        logging.debug(
            "dfs: processing edge (%d,%d), %scorrect direction, sink %s explored" 
            % ( 
                edges[edge][source],
                edges[edge][sink], 
                "" if edges[edge][source] == iU else "NOT ",
                "ALREADY" if edges[edge][sink] in explored else "NOT YET"
            )
        )
        # we have both eminating and culminating(?) edges
        # associated with each vertex, only want to follow
        # edges emmenating from this vertex
        if edges[edge][source] != iU: continue
        if edges[edge][sink] not in explored:
            logging.debug( "dfs: down the hole" )
            t = dfs(vertices,edges,edges[edge][sink],explored,leader,useF,f,s,t)

    logging.debug( "dfs: no need to recurse, incrementing t" )
    t += 1
    # only modify f if it's the first pass
    if not useF: 
        logging.debug(
            "dfs: setting f[%d] = %d" 
            % ( t,iU )
        )
        f[t] = iU
    logging.debug( "dfs: returning with t = %d" % t)
    return t

def dfs2(vertices,edges,iU,explored,leader,useF,f,s,t):

    stack = []
    logging.debug(
        "dfs2: adding %d to the stack" 
        % (iU)
    )
    stack.append(iU)

    logging.debug(
        "dfs2: marking %d as explored and setting it's leader to %d" 
        % (iU,s)
    )
    explored[iU] = 1
    leader[iU] = s

    logging.debug(
        "dfs2: using source as %s and sink as %s because useF is %s" 
        % (("source","sink","TRUE") if useF else ("sink","source","TRUE"))
    )
    (source,sink) = (0,1) if useF else (1,0)
        
    logging.debug("dfs2: entering loop over the stack")
    while len(stack) != 0:

        i = stack[-1]

        logging.debug(
            "dfs2: staring loop over %d edges for vertex %d" 
            % ( len(vertices[i]), i )
        )
        for edge in vertices[i]:
            logging.debug(
                "dfs2: processing edge (%d,%d), %scorrect direction, sink %s explored" 
                % ( 
                    edges[edge][source],
                    edges[edge][sink], 
                    "" if edges[edge][source] == i else "NOT ",
                    "ALREADY" if edges[edge][sink] in explored else "NOT YET"
                )
            )
            # we have both eminating and culminating(?) edges
            # associated with each vertex, only want to follow
            # edges emmenating from this vertex
            if edges[edge][source] != i: continue
            if edges[edge][sink] not in explored:
                logging.debug( "dfs2: appending sink %d to the stack and marking explored" )
                stack.append(edges[edge][sink])
                explored[edges[edge][sink]] = 1
                leader[edges[edge][sink]] = s
                break
        if stack[-1] == i:
            logging.debug( "dfs2: made it through the edges without adding one" )
            t += 1
            # only modify f if it's the first pass
            if not useF: 
                logging.debug(
                    "dfs2: setting f[%d] = %d" 
                    % ( t,i )
                )
                f[t] = i
            stack.pop()

    logging.debug( "dfs2: returning with t = %d" % t)
    return t

def readInput(fn):
#     pklFn = fn.replace(".txt",".pkl")
    vertices = defaultdict(list)
    nEdges = 0
    edges = {}
#     if os.path.isfile(pklFn):
#         f = open(pklFn)
#         (vertices,edges) = pickle.load( f )
#         f.close()
#     else: 
    f = open(fn)
    for line in f:
        (iU,iV) = [ int(x) for x in line.split() ]

        vertices[iU].append(nEdges)
        vertices[iV].append(nEdges)
        edges[nEdges] = [iU,iV]
        nEdges += 1
    f.close()

#         f = open(pklFn,"w")
#         pickle.dump( (vertices,edges) , f )
#         f.close()
    return (vertices,edges)


if __name__ == "__main__":
    fn = "ex1.txt" if len(sys.argv) != 2 else sys.argv[1]
    (vertices,edges) = readInput(fn)
    kosaraju(vertices,edges)
