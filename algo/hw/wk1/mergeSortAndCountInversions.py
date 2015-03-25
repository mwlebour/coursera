#!/usr/bin/env python

import unittest
import fileinput

def mwlSortAndInversions(r):
    currentLen = len(r)
    if currentLen == 0: return ([],0)
    if currentLen == 1: return (r,0)

    (rFirst,invFirst)   = mwlSortAndInversions(r[:currentLen/2])
    (rSecond,invSecond) = mwlSortAndInversions(r[currentLen/2:])
    (rSorted,invMerge) = mwlMergeAndInversions(rFirst,rSecond)
    return (rSorted,invFirst+invSecond+invMerge)

def mwlMergeAndInversions(a,b):
    inv = 0
    aLen = len(a)
    bLen = len(b)
    # in case we don't have enough mem?
    # not sure if we need it but, just in case?
    c = a[:] + b[:]
    ai = bi = 0
    for i in range(len(c)):
        if ai != aLen and (bi == bLen or a[ai] <= b[bi]):
            c[i] = a[ai]
            ai += 1
            # no inversions here
        else:
            c[i] = b[bi]
            bi += 1
            inv += aLen - ai
    return (c,inv)

def mwlSort(r):
    return mwlSortAndInversions(r)[0]

def mwlInversions(r):
    return mwlSortAndInversions(r)[1]

class TestMergeAndInversions(unittest.TestCase):

    def test_emptyVector(self):
        r = []
        self.assertEqual(mwlSort(r), r)
        self.assertEqual(mwlInversions(r), 0)
        self.assertEqual(mwlSortAndInversions(r), (r,0))

    def test_oneElementVector(self):
        r = [12]
        self.assertEqual(mwlSort(r), r)
        self.assertEqual(mwlInversions(r), 0)
        self.assertEqual(mwlSortAndInversions(r), (r,0))

    def test_simpleVector(self):
        r = [1,3,5,2,4,6]
        self.assertEqual(mwlSort(r), sorted(r))
        self.assertEqual(mwlInversions(r), 3)
        self.assertEqual(mwlSortAndInversions(r), (sorted(r),3))

    def test_tougherVector(self):
        r = [1,3,5,7,9,11,13,15,2,4,6,8,10,12,14,16,17]
        self.assertEqual(mwlSort(r), sorted(r))
        self.assertEqual(mwlInversions(r), 28)
        self.assertEqual(mwlSortAndInversions(r), (sorted(r),28))

#     def test_r1000(self):
#         r = []
#         for line in fileinput.input():
#             r.append(int(line.strip()))
#         print r
#         self.assertEqual(mwlSort(r), sorted(r))

if __name__ == '__main__':
#     unittest.main()
    r = []
    for line in fileinput.input():
        r.append(int(line.strip()))
    print mwlInversions(r)


