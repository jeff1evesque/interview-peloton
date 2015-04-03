#!/usr/bin/python

## @utility.py
#  This file contains functions that sort, and merge lists.

## qsort: sort a list in linear time using qsort algorithm.
def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

## linear_merge: merge two lists in linear time.
def linear_merge(list1, list2, sorted=True):
    # local variables
    result = []

    # sort each list, if not sorted
    if not sorted:
        list1 = qsort(list1)
        list2 = qsort(list2)

    # merge the two lists
    while list1 and list2:
        if list1[-1] > list2[-1]:
            result.append(list1.pop())
        else:
            result.append(list2.pop())
    result+=(list1+list2)[::-1]
    result.reverse()

    # return merged list
    return result
