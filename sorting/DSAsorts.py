#
# Data Structures and Algorithms COMP1002
#
# Python file to hold all sorting methods
#

import numpy as np

def bubbleSort(A):
    passnum = 0
    sorted = False
    while not sorted:
        sorted = True
        for ii in range(0, len(A) - passnum - 1):
            if A[ii] > A[ii+1]:
                temp = A[ii]
                A[ii] = A[ii+1]
                A[ii+1] = temp
                sorted = False
        passnum = passnum + 1
    return

def insertionSort(A):
    for nn in range(1, len(A)):
        ii = nn
        while (ii>0) and (A[ii-1] > A[ii]):
            temp = A[ii]
            A[ii] = A[ii-1]
            A[ii-1] = temp
            ii = ii - 1
    return


def selectionSort(A):
    for nn in range(0, len(A)):
        minIdx = nn
        for jj in range(nn+1, len(A)):
            if (A[jj] < A[minIdx]):
                minIdx = jj
        temp = A[minIdx]
        A[minIdx] = A[nn]
        A[nn] = temp
    return


def mergeSort(A):
    """ mergeSort - front-end for kick-starting the recursive algorithm
    """
    mergeSortRecurse(A, 0, len(A)-1)
    return
    ...

def mergeSortRecurse(A, leftIdx, rightIdx):
    if (leftIdx < rightIdx):
        midIdx = (leftIdx + rightIdx)//2

        mergeSortRecurse(A, leftIdx, midIdx)
        mergeSortRecurse(A, midIdx+1, rightIdx)
        merge(A, leftIdx, midIdx, rightIdx)
    return
    ...

def merge(A, leftIdx, midIdx, rightIdx):
    tempArr = np.arange(0, rightIdx - leftIdx + 1, 1)
    #Must use arange here, why?
    #tempArr = (rightIdx - leftIdx + 1)
    ii = leftIdx
    jj = midIdx + 1
    kk = 0

    while (ii <= midIdx) and (jj <= rightIdx):
        if (A[ii] <= A[jj]):
            tempArr[kk] = A[ii]
            ii = ii + 1
        else:
            tempArr[kk] = A[jj]
            jj = jj + 1
        kk = kk + 1
    
    for ii in range(ii, midIdx+1):
        tempArr[kk] = A[ii]
        kk = kk + 1

    for jj in range(jj, rightIdx+1):
        tempArr[kk] = A[jj]
        kk = kk + 1

    for kk in range(leftIdx, rightIdx+1):
        A[kk] = tempArr[kk - leftIdx]
    return
    ...

#def merge(A, leftIdx, midIdx, rightIdx):
#    L = A[leftIdx:midIdx]
#    R = A[midIdx:rightIdx+1]
#    L.append(99999999)
#    R.append(99999999)
#    ii = jj = 0
#    for kk in range(leftIdx, rightIdx+1):
#        if L[ii] <= R[jj]:
#            A[kk] = L[ii]
#            i += 1
#        else:
#            A[kk] = R[jj]
#            jj += 1
#

def quickSort(A):
    """ quickSort - front-end for kick-starting the recursive algorithm
    """
    quickSortRecurse(A, 0, len(A)-1)
    return
    ...

def quickSortRecurse(A, leftIdx, rightIdx):
    if (rightIdx > leftIdx):
        pivotIdx = (leftIdx + rightIdx)//2
        newPivotIdx = doPartitioning(A, leftIdx, rightIdx, pivotIdx)

        quickSortRecurse(A, leftIdx, newPivotIdx-1)
        quickSortRecurse(A, newPivotIdx+1, rightIdx)
    return
    ...
    
def doPartitioning(A, leftIdx, rightIdx, pivotIdx):
    pivotVal = A[pivotIdx]
    A[pivotIdx] = A[rightIdx]
    A[rightIdx] = pivotVal
    currIdx = leftIdx

    for ii in range(leftIdx, rightIdx):
        if A[ii] < pivotVal:
            temp = A[ii]
            A[ii] = A[currIdx]
            A[currIdx] = temp
            currIdx = currIdx + 1

    newPivotIdx = currIdx
    A[rightIdx] = A[newPivotIdx]
    A[newPivotIdx] = pivotVal
    return newPivotIdx

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size: ", sublistcount, "The list is: ", alist)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for ii in range(start + gap, len(alist), gap):
        currentvalue = alist[ii]
        position = ii

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


def countingSort(array, maxval):
    """countingSort is in-place counting sort"""
    n = len(array)
    m = maxval + 1
    count = [0] * m     #init with zeroes
    for a in array:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            array[i] = a
            i += 1
    return array


def radixSort(array):
    n = len(array)
    d = len(str(max(array)))

    for jj in range(1, d + 1):
        output = np.empty(n, dtype = int)
        count = np.zeros(10, dtype = int)
        for a in array:
            key = (int(a) // 10**(jj-1)) % 10
            count[key] += 1

        for ii in range(1, 10):
            count[ii] += count[ii - 1]

        for ii in range(n-1, -1, -1):
            key = (int(array[ii]) // 10**(jj-1)) % 10
            output[count[key] - 1] = array[jj]
            count[key] -= 1

        for ii in range(n):
            array[ii] = output[ii]



...
