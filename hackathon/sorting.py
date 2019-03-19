def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    for i in range(0,len(items)-1):
        for j in range(0,len(items)-1-i):
            if items[j]>items[j+1]:
                items[j],items[j+1]=items[j+1],items[j]
                print(i,j)
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) < 2:
        return items
    result = []
    mid = len(items) // 2
    list1 = merge_sort(items[:mid])
    list2 = merge_sort(items[mid:])
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] > list2[j]:
            result.append(list2[j])
            j += 1
        else:
            result.append(list1[i])
            i += 1
    result += list1[i:]
    result += list2[j:]
    return result

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items) == 1 or len(items) == 0:
        return items
    else:
        pivot = items[0]
        i = 0
        for j in range(len(items)-1):
            if items[j+1] < pivot:
                items[j+1],items[i+1] = items[i+1], items[j+1]
                i += 1
        items[0],items[i] = items[i],items[0]
        first_part = quick_sort(items[:i])
        second_part = quick_sort(items[i+1:])
        first_part.append(items[i])
        return first_part + second_part
