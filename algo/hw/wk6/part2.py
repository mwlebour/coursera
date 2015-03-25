#!/usr/bin/env python

import heapq,sys

def hiPush(h,i):
    heapq.heappush(h,i)
def loPush(h,i):
    heapq.heappush(h,-1*i)
def hiPop(h):
    return heapq.heappop(h)
def loPop(h):
    return -1 * heapq.heappop(h)
def hiMin(h):
    return h[0]
def loMax(h):
    return -1 * h[0]

if __name__ == "__main__":
    fn = "median.txt" if len(sys.argv) != 2 else sys.argv[1]

    hlo = []
    hhi = []
    s = 0
    f = open(fn)
    for line in f:
        nI = int(line.strip())

        # for the first one
        if len(hlo) == 0 and len(hhi) == 0:
            loPush(hlo,nI)
        elif len(hhi) == 0:
            if nI > loMax(hlo):
                hiPush(hhi,nI)
            else:
                hiPush(hhi,loPop(hlo))
                loPush(hlo,nI)
        else:
            if nI > hiMin(hhi):
                hiPush(hhi,nI)
            else:
                loPush(hlo,nI)

            # will keep hlo with equal or +1 wrt hhi
            # then median is always just hlo[0]
            while  len(hhi) - len(hlo) > 0:
                loPush(hlo,hiPop(hhi))
            while  len(hlo) - len(hhi) > 1:
                hiPush(hhi,loPop(hlo))

        s += loMax(hlo)
#         print len(hlo), len(hhi), -1 if len(hhi) == 0 else hiMin(hhi), loMax(hlo), s, s % 10000
    f.close()
    print s, s % 10000


# hlo - extract max
# hhi - extract min
# maintain invariant that i/2 smallest (largest) elmeents in hlo (hhi)
# median = top node of whichever has more elements or both if they have the same
# else if the same N, then top node of hlo
