def binary_chop(alist, data):
    """
    非递归解决二分查找, 比它要找的数大一点的那个位置(前提是这个数没有在里面，如果在里面则，定位它的位置)
    :param alist:
    :return:
    """
    n = len(alist)
    first = 0
    last = n - 1
    mid = 0
    while first <= last:
        mid = (last + first) // 2
        if alist[mid] > data:
            last = mid - 1
        elif alist[mid] < data:
            first = mid + 1
        else:
            first = mid
            break
    return first


list1 = [2, 4, 5, 8]
print(binary_chop(list1, 7))
print(binary_chop(list1, 2))
