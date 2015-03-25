#!/usr/bin/env python

import unittest
import fileinput

def choosePivot(r,start,end,mode = 0):
    if mode == 0:
        return start
    elif mode == 1:
        return end
    else:
        m = start + (end-start)/2
        a = [ (start,r[start]), (m,r[m]), (end,r[end]) ]
        a.sort(key=lambda x: x[1])
        return a[1][0]

def swap(r,i,j):
    t = r[i]
    r[i] = r[j]
    r[j] = t

def partition(r,start,end):
    p = r[start]
    i = start + 1
    for j in range(start+1,end+1):
        if r[j] < p:
            swap(r,i,j)
            i += 1
    swap(r,start,i-1)
    return i-1

def quickSort(r,start = -1,end = -1,pivType=0):

    if start == -1: start = 0
    if end   == -1: end = len(r)-1
    currentLen = end - start + 1

    if currentLen == 2: 
        if r[start] > r[end]:
            swap(r,start,end)
        return 1
    if currentLen == 1: return 0

    # should never be 0 due to the check before the recursive calls
    if currentLen == 0: 
        print "start=%5d end=%5d" % (start,end) ,
        print " currentLen=%5d" % (currentLen)
        return 0

    pivot = choosePivot(r,start,end,pivType)
    if pivot != start:
        swap(r,start,pivot)
            
#     print "start=%5d end=%5d" % (start,end) ,
#     print " pivot=%5d currentLen=%5d" % (pivot,currentLen),
    pivot = partition(r,start,end)
#     print " newpivot=%5d" % pivot,
#     print " r {%d,%d,%d}" % (r[start],r[start+1],r[end])
    compsA = compsB = 0
    # stay in bounds, also no need to sort if we're at the 
    # beginning or the end
    if pivot != start: compsA = quickSort(r,start,pivot-1,pivType)
    if pivot != end:   compsB = quickSort(r,pivot+1,end,pivType)
    return end - start + compsA + compsB

class TestQuickSort(unittest.TestCase):

    def test_oneElementVector(self):
        r = [12]
        rprime = r[:]
        comps = quickSort(rprime)
        self.assertEqual(comps, 0)
        self.assertEqual(r,rprime)

    def test_twoElementVector(self):
        r = [12,11]
        rprime = r[:]
        comps = quickSort(rprime)
        self.assertEqual(comps, 1)
        self.assertEqual(r,rprime)


if __name__ == '__main__':
#     unittest.main()
    r = []
    for line in fileinput.input():
        r.append(int(line.strip()))

    for  i in [0,1,2]:
        a = r[:]
        print quickSort(a,-1,-1,i)
        f = open("%d.out" % i,"w")
        for x in a:
            print >> f, x
        f.close()
