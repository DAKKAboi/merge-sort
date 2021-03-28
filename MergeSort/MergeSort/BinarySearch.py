def binarySearch(list, item):#list is an ordered list, item is what is being searched for
    length = len(list)


    def iterator(min, max):
        mid = math.floor((min+max)/2)

        if list[mid] == item:
            return mid
        elif list[mid] < item:
            mid = iterator(mid + 1, max)
        else:
            mid = iterator(min, mid - 1)
        if min == max and min != item:
            mid = -1
        return mid

    if item > list[-1] or item < list[0]:
        return None
    else:
        return iterator(0, length - 1)


