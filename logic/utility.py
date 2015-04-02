def qsort(inlist):
    if inlist == []:
        return []
    else:
        pivot = inlist[0]
        lesser = qsort([x for x in inlist[1:] if x < pivot])
        greater = qsort([x for x in inlist[1:] if x >= pivot])
        return lesser + [pivot] + greater

def linear_merge(list1, list2):
    result = []
    while list1 and list2:
        if list1[-1] > list2[-1]:
            result.append(list1.pop())
        else:
            result.append(list2.pop())
    result+=(list1+list2)[::-1]
    result.reverse()
    return result
